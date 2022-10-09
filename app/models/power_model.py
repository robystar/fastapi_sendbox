from sqlmodel import Field, Relationship, UniqueConstraint
from typing import Optional, List
from app.models.base_uuid_model import SQLModel
from app.models.links_model import LinkPowerHero

class PowerBase(SQLModel):
    name: str = Field(index=True)
    description: str
    
class Power(PowerBase, table=True):   
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    heroes: List["Hero"] = Relationship(back_populates="powers", link_model=LinkPowerHero, sa_relationship_kwargs={"lazy": "selectin"})  
