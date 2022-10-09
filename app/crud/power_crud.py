from typing import Optional
from app.schemas.power_schema import IPowerCreate, IPowerUpdate
from app.crud.base_crud import CRUDBase
from app.models.power_model import Power
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDPower(CRUDBase[Power, IPowerCreate, IPowerUpdate]):
    async def get_power_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Power:
        db_session = db_session or db.session
        power = await db_session.execute(select(Power).where(Power.name == name))
        return power.scalar_one_or_none()

power = CRUDPower(Power)
