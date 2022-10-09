from sqlmodel import Field, Relationship, UniqueConstraint
from typing import Optional, List
from app.models.base_uuid_model import SQLModel
from app.models.links_model import LinkWeaponTeam
from uuid import UUID

class WeaponBase(SQLModel):
    name: str = Field(index=True)
    description: str
    
class Weapon(WeaponBase, table=True):    
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    teams: List["Team"] = Relationship(back_populates="weapons", link_model=LinkWeaponTeam, sa_relationship_kwargs={"lazy": "selectin"})  
