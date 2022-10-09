from typing import Optional
from app.schemas.attivita_schema import IAttivitaCreate, IAttivitaUpdate
from app.crud.base_crud import CRUDBase
from app.models.attivita_model import Attivita
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDAttivita(CRUDBase[Attivita, IAttivitaCreate, IAttivitaUpdate]):
    async def get_attivita_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Attivita:
        db_session = db_session or db.session
        attivita = await db_session.execute(select(Attivita).where(Attivita.name == name))
        return attivita.scalar_one_or_none()
    
    async def get_attivita_by_id(self, *, id: int, db_session: Optional[AsyncSession] = None) -> Attivita:
        db_session = db_session or db.session
        import pdb;pdb.set_trace()
        attivita = await db_session.execute(select(Attivita).where(Attivita.idattivita == id))
        return attivita.scalar_one_or_none()
    
attivita = CRUDAttivita(Attivita)
