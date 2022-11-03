from sqlmodel import Field, Relationship
from typing import Optional
from app.models.base_uuid_model import BaseIDModel, SQLModel
from uuid import UUID

class LinkGroupUser(SQLModel, table=True):
    __table_args__ = {'schema': 'admin'}
    id: int = Field(primary_key=True, index=True, nullable=False)    
    group_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="admin.group.id", primary_key=True)
    user_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="admin.user.id", primary_key=True)

class LinkPraticaUser(SQLModel, table=True):
    __table_args__ = {'schema': 'edilizia'}
    id: int = Field(primary_key=True, index=True, nullable=False)
    pratica_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.pratica.id", primary_key=True)
    user_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="admin.user.id", primary_key=True)
    
class LinkIstanzaPratica(SQLModel, table=True):
    __table_args__ = {'schema': 'edilizia'}
    id: int = Field(primary_key=True, index=True, nullable=False)
    istanza_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.istanza.id", primary_key=True)
    pratica_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.pratica.id", primary_key=True)
    
class LinkIstanzaUser(SQLModel, table=True):
    __table_args__ = {'schema': 'edilizia'}
    id: int = Field(primary_key=True, index=True, nullable=False)
    istanza_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.istanza.id", primary_key=True)
    user_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="admin.user.id", primary_key=True) 

class LinkRecipeIngredient(SQLModel, table=True):
    __table_args__ = {'schema': 'ricette'}
    id: int = Field(primary_key=True, index=True, nullable=False)
    recipe_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="ricette.recipe.id", primary_key=True)
    ingredient_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="ricette.ingredient.id", primary_key=True)
    
    
'''
class LinkTeamHero(SQLModel, table=True):
    team_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Team.id", primary_key=True)
    hero_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Hero.id", primary_key=True)
    
class LinkPowerHero(SQLModel, table=True):
    power_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Power.id", primary_key=True)
    hero_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Hero.id", primary_key=True)  
    
class LinkWeaponTeam(SQLModel, table=True):
    weapon_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Weapon.id", primary_key=True)
    team_id: Optional[int] = Field(default=None, nullable=False, foreign_key="Team.id", primary_key=True)     


class LinkTeamHero(BaseJoinUUIDModel, table=True):
    team_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Team.id", primary_key=True)
    hero_id: Optional[UUID] = Field(default=None, nullable=False, foreign_key="Hero.id", primary_key=True)
    is_training: bool = False

    team: "Team" = Relationship(back_populates="heroes", sa_relationship_kwargs={"lazy": "selectin"})
    hero: "Hero" = Relationship(back_populates="teams", sa_relationship_kwargs={"lazy": "selectin"})
'''