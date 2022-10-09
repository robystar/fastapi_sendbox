from typing import Optional, List

from app.models.hero_model import HeroBase
from app.models.team_model import TeamBase, Team
from app.models.power_model import PowerBase, Power
from app.schemas.power_schema import IPowerCreate, IPowerRead
from app.schemas.team_schema import ITeamCreate, ITeamRead
from uuid import UUID

class IHeroCreate(HeroBase):
    pass

class IHeroCreateWithPowersAndTeams(HeroBase):
    teams: List[ITeamCreate]
    powers: List[IPowerCreate]

class IHeroRead(HeroBase):
    id: UUID

class IHeroUpdate(HeroBase):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None

class IHeroReadWithTeams(IHeroRead):
    teams: List[ITeamRead]
    powers: List[IPowerRead]


class IHeroReadWithPowersAndTeam(IHeroRead):
    teams: List[ITeamRead]
    powers: List[IPowerRead]

class IHeroReadWithPowers(IHeroRead):
    powers: List[PowerBase]