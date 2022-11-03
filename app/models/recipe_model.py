from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship, Column, DateTime
from app.models.links_model import LinkRecipeIngredient
from typing import List, Optional
from pydantic import EmailStr
from app.models.base_uuid_model import BaseJoinUUIDModel, BaseUUIDModel
from uuid import UUID

class RecipeBase(SQLModel):
    name: str
    description: str
    imagePath: Optional[str]
    
class Recipe(BaseUUIDModel, RecipeBase, table=True):   
    __table_args__ = {'schema': 'ricette'}
    created_by_id: Optional[UUID] = Field(default=None, foreign_key="admin.user.id")
    created_by: "User" = Relationship(sa_relationship_kwargs={"lazy":"selectin"})        
    ingredients: List["Ingredient"] = Relationship(back_populates="recipes", link_model=LinkRecipeIngredient, sa_relationship_kwargs={"lazy": "selectin"})


class IngredientBase(SQLModel):
    name: str
    amount: float
    
class Ingredient(BaseJoinUUIDModel, IngredientBase, table=True):   
    __table_args__ = {'schema': 'ricette'}
    recipes: List["Recipe"] = Relationship(back_populates="ingredients", link_model=LinkRecipeIngredient, sa_relationship_kwargs={"lazy": "selectin"})
