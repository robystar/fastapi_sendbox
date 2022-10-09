from app.models.hero_model import HeroBase
from typing import List, Optional
from app.models.weapon_model import WeaponBase
from app.models.team_model import TeamBase
from pydantic import BaseModel
from uuid import UUID

class IWeaponRead(WeaponBase):
    id: int

class IWeaponCreate(WeaponBase):
    pass

class IWeaponUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class IWeaponReadWithTeams(IWeaponRead):
    heroes: List[TeamBase]

    