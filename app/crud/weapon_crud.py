from typing import Optional
from app.schemas.weapon_schema import IWeaponCreate, IWeaponUpdate
from app.crud.base_crud import CRUDBase
from app.models.weapon_model import Weapon
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDWeapon(CRUDBase[Weapon, IWeaponCreate, IWeaponUpdate]):
    async def get_weapon_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Weapon:
        db_session = db_session or db.session
        weapon = await db_session.execute(select(Weapon).where(Weapon.name == name))
        return weapon.scalar_one_or_none()

weapon = CRUDWeapon(Weapon)