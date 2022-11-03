from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import Optional, List
from app.models.base_uuid_model import BaseIDModel
from uuid import UUID
from datetime import datetime

from app.models.links_model import LinkIstanzaPratica, LinkPraticaUser


class PraticaBase(SQLModel):
    numero_pratica: str = Field(default=None)
    data_presentazione: datetime = Field(default=None)
    tipo_pratica: str = Field(default=None)
    anno_pratica: int = Field(default=None)
    tipo_intervento: str = Field(default=None)
    tipo_procedimento: str = Field(default=None)
    oggetto: str = Field(default=None)
    intervento: str = Field(default=None)
    note: str = Field(default=None)
    

class Pratica(BaseIDModel, PraticaBase, table=True):  
    __table_args__ = {'schema': 'edilizia'}
    created_by_id: Optional[UUID] = Field(default=None, foreign_key="admin.user.id")
    created_by: "User" = Relationship(sa_relationship_kwargs={"lazy":"selectin"})    
    owners: List["User"] = Relationship(back_populates="pratiche", link_model=LinkPraticaUser, sa_relationship_kwargs={"lazy": "selectin"})    
    istanze: List["Istanza"] = Relationship(back_populates="pratiche", link_model=LinkIstanzaPratica, sa_relationship_kwargs={"lazy": "selectin"})    
