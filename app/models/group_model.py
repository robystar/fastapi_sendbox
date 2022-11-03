from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional
from app.models.links_model import LinkGroupUser
from app.models.base_uuid_model import BaseUUIDModel
from uuid import UUID

class GroupBase(SQLModel):
    name: str
    description: str

class Group(BaseUUIDModel, GroupBase, table=True):    
    __table_args__ = {'schema': 'admin'}
    created_by_id: Optional[UUID] = Field(default=None, foreign_key="admin.user.id")
    created_by: "User" = Relationship(sa_relationship_kwargs={"lazy":"selectin"})    
    users: List["User"] = Relationship(back_populates="groups", link_model=LinkGroupUser, sa_relationship_kwargs={"lazy": "selectin"})




