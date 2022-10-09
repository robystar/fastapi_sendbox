from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List
from app.models.base_uuid_model import BaseUUIDModel
from app.models.links_model import LinkTeamHero, LinkPowerHero
from uuid import UUID

class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

class Hero(BaseUUIDModel, HeroBase, table=True):    
    created_by_id: Optional[UUID] = Field(default=None, foreign_key="User.id")
    created_by: "User" = Relationship(sa_relationship_kwargs={"lazy":"selectin", "primaryjoin":"Hero.created_by_id==User.id"})
    powers: List["Power"] = Relationship(back_populates="heroes", link_model=LinkPowerHero, sa_relationship_kwargs={"lazy": "joined"})
    teams: List["Team"] = Relationship(back_populates="heroes", link_model=LinkTeamHero, sa_relationship_kwargs={"lazy": "selectin"})

