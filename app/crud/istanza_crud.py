from datetime import datetime
from typing import List, Optional, Union
from app.models.istanza_model import Istanza
from app.models.soggetto_model import Delegato, Richiedente, Tecnico, Giuridica, Domicilio
from app.models.ubicazione_model import Civico, Mappale_nceu, Mappale_nct, Posizione
from app.models.user_model import User
from app.schemas.istanza_schema import IIstanzaCreate, IIstanzaUpdate, IIstanzaCreateAll, IIstanzaUpdateAll
from app.crud.base_crud import CRUDBase
from fastapi_async_sqlalchemy import db
from sqlmodel import select, delete
from uuid import UUID
from app import crud
from sqlmodel.ext.asyncio.session import AsyncSession

from app.schemas.soggetto_schema import IRichiedenteUpdate, ITecnicoCreate, ITecnicoUpdate
from app.schemas.ubicazione_schema import IUbicazioneCreate

class CRUDIstanza(CRUDBase[Istanza, IIstanzaCreate, IIstanzaUpdate]):
    
    #Metodo principale che allinea la form di plomino con istanza e richiedenti frm_tipoapp
    async def update_istanza_with_richiedenti(
        self,
        *,
        obj_in: Union[IIstanzaCreateAll, Istanza],
        istanza_id: int,
        created_by_id: Optional[Union[UUID, str]] = None,
        db_session: Optional[AsyncSession] = None,
    ) -> IIstanzaUpdateAll:
        db_session = db_session or db.session

        db_istanza = await super().get(id=istanza_id)
        
        if not db_istanza:
            db_istanza = Istanza.from_orm(obj_in)  # type: ignore
            if created_by_id:
                db_istanza.created_by_id = created_by_id
                db_istanza.created_at = datetime.utcnow()
        else:
            await db_session.execute(delete(Richiedente).where(Richiedente.istanza_id == db_istanza.id))
            await db_session.execute(delete(Delegato).where(Delegato.istanza_id == db_istanza.id))
            await db_session.commit()
            await db_session.refresh(db_istanza)
            
        for richiedente_in in obj_in.richiedenti:
            richiedente_db = Richiedente.from_orm(richiedente_in)
            richiedente_db.istanza_id = istanza_id
            db_session.add(richiedente_db)

            if richiedente_in.giuridica:
                richiedente_db.giuridica = Giuridica.from_orm(richiedente_in.giuridica)
            if richiedente_in.domicilio:
                richiedente_db.domicilio = Domicilio.from_orm(richiedente_in.domicilio)                
            db_istanza.richiedenti.append(richiedente_db)
            
        db_istanza.delegato = Delegato.from_orm(obj_in.delegato)
        
        db_istanza.updated_at = datetime.utcnow()
        
        db_session.add(db_istanza)
        await db_session.commit()
        await db_session.refresh(db_istanza)
        return db_istanza    
    

    async def update_richiedenti_istanza(self, *, richiedenti: List[IRichiedenteUpdate], db_istanza: Istanza, db_session: Optional[AsyncSession] = None) -> Istanza:
        
        db_session = db_session or db.session
                
        await db_session.execute(delete(Richiedente).where(Richiedente.istanza_id == db_istanza.id))
        await db_session.commit()
        await db_session.refresh(db_istanza)
        
        
        richiedenti_db = []
        for richiedente_in in richiedenti:
            richiedente_db = Richiedente.from_orm(richiedente_in)
            db_session.add(richiedente_db)
            if richiedente_in.giuridica:
                richiedente_db.giuridica = Giuridica.from_orm(richiedente_in.giuridica)
            if richiedente_in.domicilio:
                richiedente_db.domicilio = Domicilio.from_orm(richiedente_in.domicilio)                
            richiedenti_db.append(richiedente_db)    
            
        db_istanza.richiedenti=richiedenti_db
        db_session.add(db_istanza)
        
        await db_session.commit()
        await db_session.refresh(db_istanza)
        return db_istanza  



    async def update_tecnici_istanza(self, *, tecnici: List[ITecnicoUpdate], db_istanza: Istanza, db_session: Optional[AsyncSession] = None) -> Istanza:
        
        db_session = db_session or db.session
                
        for tecnico in db_istanza.tecnici:
            await db_session.delete(tecnico)
            
        db_istanza.tecnici=[Tecnico.from_orm(tecnico) for tecnico in tecnici]
        db_session.add(db_istanza)
        
        await db_session.commit()
        await db_session.refresh(db_istanza)
        return db_istanza      
    
    
    async def update_ubicazione_istanza(self, *, ubicazione: IUbicazioneCreate, db_istanza: Istanza, db_session: Optional[AsyncSession] = None) -> Istanza:

        db_session = db_session or db.session
        
        for civico in db_istanza.civici:
            await db_session.delete(civico)
        for mappale in db_istanza.nct:
            await db_session.delete(mappale)            
        for mappale in db_istanza.nceu:
            await db_session.delete(mappale) 
        if db_istanza.posizione:            
            await db_session.delete(db_istanza.posizione)
        
        db_istanza.posizione = Posizione.from_orm(ubicazione.posizione)
        
        for civico_in in ubicazione.civici:
            civico_in.geom_p = 'SRID=4326;POINT(%s)' %civico_in.geom_p
            db_istanza.civici.append(Civico.from_orm(civico_in))
        
        for mappale_in in ubicazione.nct:
            mappale_in.geom_plg = 'SRID=4326;%s' %mappale_in.geom_plg
            db_istanza.nct.append(Mappale_nct.from_orm(mappale_in))
        
        db_istanza.nceu=[Mappale_nceu.from_orm(obj) for obj in ubicazione.nceu]
       
        db_session.add(db_istanza)
        await db_session.commit()
        await db_session.refresh(db_istanza)
        return istanza  


    async def add_user_to_istanza(self, *, user: User, istanza_id: int) -> Istanza:
        istanza = await super().get(id=istanza_id)
        istanza.users.append(user)        
        db.session.add(istanza)
        await db.session.commit()
        await db.session.refresh(istanza)
        return istanza

    async def add_users_to_istanza(self, *, users: List[User], istanza_id: int, db_session: Optional[AsyncSession] = None) -> Istanza:
        db_session = db_session or db.session
        istanza = await super().get(id=istanza_id, db_session=db_session)
        istanza.users.extend(users)        
        db_session.add(istanza)
        await db_session.commit()
        await db_session.refresh(istanza)
        return istanza








istanza = CRUDIstanza(Istanza)
