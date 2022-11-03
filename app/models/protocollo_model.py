from sqlmodel import Field, SQLModel, Relationship, Column, DateTime
from typing import Optional, List
from datetime import datetime

class ProtocolloBase(SQLModel):
    
    data_protocollo: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=True))
    flusso: str = Field(default=None)
    numero_fascicolo: int = Field(default=None)
    anno_fascicolo: int = Field(default=None)
    classifica: str = Field(default=None)
    tipo_documento: str = Field(default=None)
    uo: str = Field(default=None)
    
    
class Protocollo(ProtocolloBase, table=True):   
    __table_args__ = {'schema': 'edilizia'}    
    numero_protocollo: Optional[int] = Field(default=None, primary_key=True)
