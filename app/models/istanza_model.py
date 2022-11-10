from sqlmodel import SQLModel, Field, Relationship, Column, DateTime, UniqueConstraint, JSON, ARRAY, String, ForeignKey
from typing import Dict, Optional, List
from app.models.base_uuid_model import BaseIDModel
from uuid import UUID
from datetime import datetime



from app.models.links_model import LinkIstanzaUser
from app.models.links_model import LinkIstanzaPratica


class IstanzaBase(SQLModel):
    data_creazione: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=True))
    data_presentazione: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=True))
    readers: List[str] | None = Field(sa_column=Column(ARRAY(String), nullable=True))
    authors: List[str] | None = Field(sa_column=Column(ARRAY(String), nullable=True))
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
    richiedenti: List["Richiedente"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin"})    
    delegato: Optional["Delegato"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin", "uselist":False})  
    tecnici: List["Tecnico"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin"})
    posizione: Optional["Posizione"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin", "uselist":False})
    civici: List["Civico"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin"})   
    nct: List["Mappale_nct"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin"}) 
    nceu: List["Mappale_nceu"] = Relationship(back_populates="istanza", sa_relationship_kwargs={"lazy": "selectin"}) 
    
    
class JSONDataBase(SQLModel):   
    data: Dict = Field(default={}, sa_column=Column(JSON))

class Intervento(JSONDataBase, table=True):
    __table_args__ = {'schema': 'edilizia'}
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), primary_key=True, nullable=False, default=None))
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    class Config:
        arbitrary_types_allowed = True
        
class Asseverazioni(JSONDataBase, table=True):
    __table_args__ = {'schema': 'edilizia'}
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), primary_key=True, nullable=False, default=None))
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    class Config:
        arbitrary_types_allowed = True        
        
class Vincoli(JSONDataBase, table=True):
    __table_args__ = {'schema': 'edilizia'}
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), primary_key=True, nullable=False, default=None))
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    class Config:
        arbitrary_types_allowed = True
        
class IJSONDataCreate(JSONDataBase):
    istanza_id: Optional[int]
