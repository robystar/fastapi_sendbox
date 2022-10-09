from app.models.weapon_model import Weapon
from app.models.hero_model import HeroBase
from typing import List, Optional
from app.models.team_model import TeamBase
from pydantic import BaseModel
from uuid import UUID

class ITeamRead(TeamBase):
    id: int

class ITeamCreate(TeamBase):
    pass

class ITeamCreateWithWeapons(TeamBase):
    weapons: List[Weapon]

class ITeamUpdate(BaseModel):
    name: Optional[str] = None
    headquarters: Optional[str] = None

class ITeamReadWithHeroes(ITeamRead):
    heroes: List[HeroBase]

    