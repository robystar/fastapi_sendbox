from datetime import datetime
from typing import List, Optional, Union
from app.models.istanza_model import Istanza
from app.models.soggetto_model import Delegato, Giuridica, Richiedente, Tecnico
from app.models.ubicazione_model import Civico, Mappale_nceu, Posizione
from app.models.user_model import User
from app.schemas.istanza_schema import IIstanzaCreate, IIstanzaUpdate, IIstanzaCreateAll, IIstanzaUpdateAll
from app.crud.base_crud import CRUDBase
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from uuid import UUID
from app import crud
from sqlmodel.ext.asyncio.session import AsyncSession

from app.schemas.soggetto_schema import ITecnicoCreate, IRichiedenteReadAll
from app.schemas.ubicazione_schema import IUbicazioneCreate

class CRUDIstanza(CRUDBase[Istanza, IIstanzaCreate, IIstanzaUpdate]):
    async def get_istanza_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Istanza:
        db_session = db_session or db.session
        istanza = await db_session.execute(select(Istanza).where(Istanza.name == name))
        return istanza.scalar_one_or_none()
 
    async def create_istanza_with_id(
        self,
        *,
        obj_in: Union[IIstanzaCreateAll, Istanza],
        istanza_id: int,
        created_by_id: Optional[Union[UUID, str]] = None,
        db_session: Optional[AsyncSession] = None,
    ) -> IIstanzaCreateAll:
        db_session = db_session or db.session
        import pdb;pdb.set_trace()
        db_istanza = Istanza.from_orm(obj_in)  # type: ignore
        
        if created_by_id:
            db_istanza.created_by_id = created_by_id
            db_istanza.created_at = datetime.utcnow()
            db_istanza.updated_at = datetime.utcnow()
        
        db_istanza.id = istanza_id
        
        for richiedente in obj_in.richiedenti:
            db_richiedente = Richiedente.from_orm(richiedente)
            db_session.add(db_richiedente)
            db_richiedente.giuridica = Giuridica.from_orm(richiedente.giuridica)
            db_istanza.richiedenti.append(db_richiedente)
        
        
        
                

        
        db_istanza.delegato = Delegato.from_orm(obj_in.delegato)
        db_session.add(db_istanza)
        await db_session.commit()
        await db_session.refresh(db_istanza)
        return db_istanza
    
    async def update_istanza_with_id(
        self,
        *,
        obj_in: Union[IIstanzaUpdateAll, Istanza],
        istanza_id: int,
        db_session: Optional[AsyncSession] = None,
    ) -> IIstanzaUpdateAll:
        db_session = db_session or db.session
        import pdb;pdb.set_trace()
        new_istanza = Istanza.from_orm(obj_in)  # type: ignore
        
        db_istanza = await super().get(id=istanza_id)
        

        for richiedente in db_istanza.richiedenti:
            await db_session.delete(richiedente)
        await db_session.delete(db_istanza.delegato)

        richiedenti_db=[]
        for richiedente in obj_in.richiedenti:
            richiedente.istanza_id = istanza_id
            richiedenti_db.append(Richiedente.from_orm(richiedente))     
        db_istanza.richiedenti=richiedenti_db   


        db_istanza.delegato = Delegato.from_orm(obj_in.delegato)
        db_session.add(db_istanza)
        await db_session.commit()
        await db_session.refresh(db_istanza)
        return db_istanza

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
    
       
    async def add_delegato_to_istanza(self, *, delegato: Delegato, istanza_id: int) -> Istanza:
        istanza = await super().get(id=istanza_id)
        istanza.delegato.append(delegato)        
        db.session.add(istanza)
        await db.session.commit()
        await db.session.refresh(istanza)
        return istanza   
    
    async def add_richiedente_to_istanza(self, *, richiedente: ITecnicoCreate, istanza_id: int) -> Istanza:
        
        istanza = await super().get(id=istanza_id)
        istanza.tecnici.append(richiedente)        
        db.session.add(istanza)
        await db.session.commit()
        await db.session.refresh(istanza)
        return istanza

    async def add_tecnici_to_istanza(self, *, tecnici: List[ITecnicoCreate], istanza_id: int, db_session: Optional[AsyncSession] = None) -> Istanza:
        
        ####TODO????
        db_session = db_session or db.session
        istanza = await super().get(id=istanza_id, db_session=db_session)
        istanza.tecnici.extend(tecnici)        
        db_session.add(istanza)
        await db_session.commit()
        await db_session.refresh(istanza)
        return istanza   
    
    async def update_tecnici_istanza(self, *, tecnici: List[ITecnicoCreate], istanza_id: int, db_session: Optional[AsyncSession] = None) -> Istanza:
        
        db_session = db_session or db.session

        istanza = await super().get(id=istanza_id, db_session=db_session)
        
        for tecnico in istanza.tecnici:
            await db_session.delete(tecnico)
        
        tecnici_db=[]
        for tecnico in tecnici:
            tecnico.istanza_id = istanza_id
            tecnici_db.append(Richiedente.from_orm(tecnico))     
        istanza.tecnici=tecnici_db   

        db_session.add(istanza)
        await db_session.commit()
        await db_session.refresh(istanza)
        return istanza  



    async def add_tecnico_to_istanza(self, *, tecnico: ITecnicoCreate, istanza_id: int) -> Istanza:
        
        istanza = await super().get(id=istanza_id)
        istanza.tecnici.append(tecnico)        
        db.session.add(istanza)
        await db.session.commit()
        await db.session.refresh(istanza)
        return istanza

    async def add_tecnici_to_istanza(self, *, tecnici: List[ITecnicoCreate], istanza_id: int, db_session: Optional[AsyncSession] = None) -> Istanza:
        
        ####TODO????
        db_session = db_session or db.session
        istanza = await super().get(id=istanza_id, db_session=db_session)
        istanza.tecnici.extend(tecnici)        
        db_session.add(istanza)
        await db_session.commit()
        await db_session.refresh(istanza)
        return istanza   
    
    async def update_tecnici_istanza(self, *, tecnici: List[ITecnicoCreate], istanza_id: int, db_session: Optional[AsyncSession] = None) -> Istanza:
        
        db_session = db_session or db.session

        istanza = await super().get(id=istanza_id, db_session=db_session)
        
        for tecnico in istanza.tecnici:
            await db_session.delete(tecnico)
        
        tecnici_db=[]
        for tecnico in tecnici:
            tecnico.istanza_id = istanza_id
            tecnici_db.append(Tecnico.from_orm(tecnico))     
        istanza.tecnici=tecnici_db   

        db_session.add(istanza)
        await db_session.commit()
        await db_session.refresh(istanza)
        return istanza  

    async def update_ubicazione_istanza(self, *, ubicazione: IUbicazioneCreate, istanza_id: int, db_session: Optional[AsyncSession] = None) -> Istanza:

        db_session = db_session or db.session

        istanza = await super().get(id=istanza_id, db_session=db_session)
        
        import pdb;pdb.set_trace()
        
        ubicazione.posizione.istanza_id = istanza_id
        istanza.posizione = Posizione.from_orm(ubicazione.posizione)
        istanza.posizione.istanza_id = istanza_id
        
        '''
        for nceu in istanza.nceu:
            await db_session.delete(nceu)
        '''
        nceu_db=[]
        for nceu in ubicazione.nceu:
            nceu.istanza_id = istanza_id
            nceu_db.append(Mappale_nceu.from_orm(nceu))     
        istanza.nceu=nceu_db   
        
        
        
        
        db_session.add(istanza)
        await db_session.commit()
        await db_session.refresh(istanza)
        return istanza  
    

istanza = CRUDIstanza(Istanza)
