import enum
from uuid import UUID
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint, Date, ARRAY, String
from sqlalchemy import Column, String
from typing import Optional, List
from datetime import datetime, date

class Fiscale(SQLModel):
    cf: Optional[str] = Field(sa_column=Column(String(16), nullable=True))
    piva: Optional[str] = Field(sa_column=Column(String(11), nullable=True))  

class FisicaBase(SQLModel):    
    app: Optional[str]
    nome: Optional[str]
    cognome: Optional[str]
    data_nato: Optional[date]
    comune_nato: Optional[str]
    prov_nato: Optional[str]
    loc_nato: Optional[str]
    codcat_nato: Optional[str] = Field(sa_column=Column(String(4), nullable=True, default='xxxx'))
    cittadinanza: Optional[str] # cittadinanza serve? in automatico?
    sesso: Optional[str] = Field(sa_column=Column(String(1), nullable=True, default='M'))
    search: Optional[str]
 
class Indirizzo(SQLModel):
    comune: Optional[str]
    prov:  Optional[str]
    loc: Optional[str]
    cap: Optional[str]
    indirizzo: Optional[str]
    civico: Optional[str]
    
class Recapito(SQLModel):
    email:  Optional[str]
    pec:  Optional[str]
    telefono:  Optional[str]
    cellulare:  Optional[str]
    fax:  Optional[str]

class RichiedenteBase(FisicaBase, Indirizzo, Recapito, Fiscale):
    qualita: Optional[str]
    principale: Optional[bool] = Field(default=False)
    sostituito: Optional[bool] = Field(default=False)
    
class DomicilioBase(Indirizzo):
    pass    
    
class GiuridicaBase (Indirizzo, Recapito, Fiscale):
    denominazione: Optional[str] 
    qualita: Optional[str]
    qualita_altro: Optional[str]
    
class DelegatoBase(FisicaBase, Indirizzo, Recapito, Fiscale):
    pass

class Domicilio(DomicilioBase, table=True):  
    __table_args__ = {'schema': 'edilizia'}
    richiedente_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.richiedente.id", primary_key=True)

class Giuridica(GiuridicaBase, table=True):  
    __table_args__ = {'schema': 'edilizia'}
    richiedente_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.richiedente.id", primary_key=True)

class Richiedente(RichiedenteBase, table=True):  
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    istanza_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.istanza.id")
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"joined"})
    domicilio: Optional[Domicilio] = Relationship(sa_relationship_kwargs={"lazy":"joined","uselist":False})
    giuridica: Optional[Giuridica] = Relationship(sa_relationship_kwargs={"lazy":"joined","uselist":False})
    
class Delegato(DelegatoBase, table=True):  
    __table_args__ = {'schema': 'edilizia'}
    istanza_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.istanza.id", primary_key=True)
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"joined"})


class TecnicoBase(FisicaBase, Indirizzo, Recapito, Fiscale):
    
    denominazione: Optional[str] 
    data_incarico: Optional[date]
    qualita: Optional[str]
    qualita_altro: Optional[str]
    ruolo:  List[str] = Field(sa_column=Column(ARRAY(String)))
    ruolo_altro: Optional[str]
    
    albo: Optional[str]
    albo_numero: Optional[str]
    albo_prov: Optional[str]
    
    cciaa: Optional[str]
    cciaa_numero: Optional[str]
    cciaa_prov: Optional[str]    

    edile_numero: Optional[str]
    edile_prov: Optional[str]
    inail: Optional[str]
    inps: Optional[str]
    
    indirizzo_residenza: Optional[str]
    civico_residenza: Optional[str]
    comune_residenza: Optional[str]
    prov_residenza: Optional[str]
    cap_residenza: Optional[str]

    principale: Optional[bool] = Field(default=False)
    sostituito: Optional[bool] = Field(default=False)
     
class Tecnico(TecnicoBase, table=True):  
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    istanza_id: Optional[int] = Field(default=None, nullable=False, foreign_key="edilizia.istanza.id")
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"joined"})

