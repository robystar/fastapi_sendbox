from sqlmodel import SQLModel, Relationship, Field
from typing import List
from app.models.base_uuid_model import BaseUUIDModel

class RoleBase(SQLModel):
    name: str
    description: str

class Role(BaseUUIDModel, RoleBase, table=True):  
    __table_args__ = {'schema': 'admin'}
    users: List["User"] = Relationship(back_populates="role", sa_relationship_kwargs={"lazy": "selectin"})


