from typing import Optional
from app.schemas.anagrafe_schema import IAnagrafeCreate, IAnagrafeUpdate
from app.crud.base_crud import CRUDBase
from app.models.anagrafe_model import Anagrafe
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDAnagrafe(CRUDBase[Anagrafe, IAnagrafeCreate, IAnagrafeUpdate]):
    async def get_anagrafe_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Anagrafe:
        db_session = db_session or db.session
        anagrafe = await db_session.execute(select(Anagrafe).where(Anagrafe.name == name))
        return anagrafe.scalar_one_or_none()
    
    async def get_anagrafe_by_id(self, *, id: int, db_session: Optional[AsyncSession] = None) -> Anagrafe:
        db_session = db_session or db.session
        anagrafe = await db_session.execute(select(Anagrafe).where(Anagrafe.idanagrafe == id))
        return anagrafe.scalar_one_or_none()
    

anagrafe = CRUDAnagrafe(Anagrafe)
