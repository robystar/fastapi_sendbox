from sqlmodel import Field, Relationship, UniqueConstraint
from typing import List, Optional
from typing import List
from app.models.links_model import LinkTeamHero, LinkWeaponTeam
from app.models.base_uuid_model import SQLModel

from uuid import UUID

class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str 

class Team(TeamBase, table=True):    
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    heroes: List["Hero"] = Relationship(back_populates="teams", link_model=LinkTeamHero, sa_relationship_kwargs={"lazy": "selectin"})  
    weapons: List["Weapon"] = Relationship(back_populates="teams", link_model=LinkWeaponTeam, sa_relationship_kwargs={"lazy": "selectin"}) 
