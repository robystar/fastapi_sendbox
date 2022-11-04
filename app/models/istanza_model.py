from sqlmodel import SQLModel, Field, Relationship, Column, DateTime, UniqueConstraint
from typing import Optional, List
from app.models.base_uuid_model import BaseIDModel
from uuid import UUID
from datetime import datetime

from app.models.links_model import LinkIstanzaUser
from app.models.links_model import LinkIstanzaPratica


class IstanzaBase(SQLModel):
    data_creazione: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=True))
    data_presentazione: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=True))
    tipo: Optional[str]
    tipo_altro: Optional[str]
    sportello: Optional[str]
    oggetto: Optional[str]
    intervento: Optional[str]
    consenso_pec: Optional[bool]
    firma_digitale_opt: Optional[int]
    note: Optional[str]
    

class Istanza(BaseIDModel, IstanzaBase, table=True):  
    __table_args__ = {'schema': 'edilizia'}
    created_by_id: Optional[UUID] = Field(default=None, foreign_key="admin.user.id")
    created_by: "User" = Relationship(sa_relationship_kwargs={"lazy":"selectin"}) 
       
    owners: List["User"] = Relationship(back_populates="istanze", link_model=LinkIstanzaUser, sa_relationship_kwargs={"lazy": "selectin"})    
    pratiche: List["Pratica"] = Relationship(back_populates="istanze", link_model=LinkIstanzaPratica, sa_relationship_kwargs={"lazy": "selectin"})    
    richiedenti: List["Soggetto"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin"})    
    delegato: Optional["Delegato"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin", "uselist":False})    
    tecnici: List["Soggetto"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin"})    
