from sqlmodel import Field, Relationship
from typing import Optional
from app.models.base_uuid_model import BaseJoinUUIDModel, SQLModel
from uuid import UUID

class LinkGroupUser(BaseJoinUUIDModel, table=True):
    group_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Group.id", primary_key=True)
    user_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="User.id", primary_key=True)

class LinkTeamHero(SQLModel, table=True):
    team_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Team.id", primary_key=True)
    hero_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Hero.id", primary_key=True)
    
class LinkPowerHero(SQLModel, table=True):
    power_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Power.id", primary_key=True)
    hero_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Hero.id", primary_key=True)  
    
class LinkWeaponTeam(SQLModel, table=True):
    weapon_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Weapon.id", primary_key=True)
    team_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Team.id", primary_key=True)     

'''
class LinkTeamHero(BaseJoinUUIDModel, table=True):
    team_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Team.id", primary_key=True)
    hero_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Hero.id", primary_key=True)
    is_training: bool = False

    team: "Team" = Relationship(back_populates="heroes", sa_relationship_kwargs={"lazy": "selectin"})
    hero: "Hero" = Relationship(back_populates="teams", sa_relationship_kwargs={"lazy": "selectin"})
'''