from sqlmodel import SQLModel, Field, Relationship, JSON, ForeignKey, Column
from typing import Optional, List

class PagopaImportiBase(SQLModel):
    codimp: Optional[str]
    tipo: Optional[str]
    importo: Optional[float]
    causale: Optional[str]
    scadenza: Optional[str]
    azione: Optional[str]
    
class PagopaPagamentiBase(SQLModel):
    codtrans: Optional[str]
    iuv: Optional[str]
    importo: Optional[str]
    data: Optional[str]
    alias: Optional[str]
    anagrafica: Optional[str]
    brand: Optional[str]
    divisa: Optional[str]
    email: Optional[str]
    esito: Optional[str]
    metodo: Optional[str]
    orario: Optional[str]
    uidriscossione: Optional[str]

class PagopaImporti(PagopaImportiBase, table=True): 
    __tablename__ = 'pagopa_importi'
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), nullable=False, default=None))

class PagopaPagamenti(PagopaPagamentiBase, table=True):  
    __tablename__ = 'pagopa_pagamenti'
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), nullable=False, default=None))
