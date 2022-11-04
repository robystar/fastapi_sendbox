from datetime import datetime
from typing import List, Optional, Union
from app.models.istanza_model import Istanza
from app.models.richiedente_model import Delegato, Richiedente
from app.models.user_model import User
from app.schemas.istanza_schema import IIstanzaCreate, IIstanzaUpdate, IIstanzaCreateAll
from app.crud.base_crud import CRUDBase
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession

from app.schemas.richiedente_schema import IRichiedenteReadAll

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
        db_istanza.richiedenti = [Richiedente.from_orm(richiedente) for richiedente in obj_in.richiedenti]
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
    
    
    async def add_richiedente_to_istanza(self, *, richiedente: IRichiedenteReadAll, istanza_id: int) -> Istanza:
        istanza = await super().get(id=istanza_id)
        istanza.richiedenti.append(richiedente)        
        db.session.add(istanza)
        await db.session.commit()
        await db.session.refresh(istanza)
        return istanza

    async def add_richiedenti_to_istanza(self, *, richiedenti: List[Richiedente], istanza_id: int, db_session: Optional[AsyncSession] = None) -> Istanza:
        db_session = db_session or db.session
        istanza = await super().get(id=istanza_id, db_session=db_session)
        istanza.richiedenti.extend(richiedenti)        
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
    

istanza = CRUDIstanza(Istanza)
