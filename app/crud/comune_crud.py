from typing import Optional
from app.schemas.comune_schema import IComuneCreate, IComuneUpdate
from app.crud.base_crud import CRUDBase
from app.models.comune_model import Comune
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDComune(CRUDBase[Comune, IComuneCreate, IComuneUpdate]):
    async def get_comune_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Comune:
        db_session = db_session or db.session
        comune = await db_session.execute(select(Comune).where(Comune.name == name))
        return comune.scalar_one_or_none()

comune = CRUDComune(Comune)
