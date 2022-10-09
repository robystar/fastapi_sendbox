from app.models.hero_model import HeroBase
from typing import List, Optional
from app.models.power_model import PowerBase
from pydantic import BaseModel
from uuid import UUID

class IPowerRead(PowerBase):
    id: int

class IPowerCreate(PowerBase):
    pass

class IPowerUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class IPowerReadWithHeroes(IPowerRead):
    heroes: List[HeroBase]

    