import enum
from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint, Date
from sqlalchemy import Column, String
from typing import Optional, List
from datetime import datetime, date

class SessoType(enum.Enum):
    # tolto per ora che rompe....
    M = "M"
    F = "F"

class Fiscale(SQLModel):
    cf: Optional[str] = Field(sa_column=Column(String(16), nullable=True))
    piva: Optional[str] = Field(sa_column=Column(String(11), nullable=True))  

class FisicaBase(SQLModel):    
    app: Optional[str]
    nome: Optional[str]
    cognome: Optional[str]
    data_nato: Optional[Date]
    comune_nato: Optional[str]
    prov_nato: Optional[str]
    loc_nato: Optional[str]
    codcat_nato: Optional[str] = Field(sa_column=Column(String(4), nullable=True))
    cittadinanza: Optional[str] # cittadinanza serve? in automatico?
    sesso: Optional[SessoType]

class GiuridicaBase(SQLModel):   
    denominazione: Optional[str] 

class Indirizzo(SQLModel):
    comune = Optional[str]
    prov =  Optional[str]
    loc = Optional[str]
    cap =  Optional[str]
    indirizzo = Optional[str]
    civico = Optional[str]
    
class Recapito(SQLModel):
    email =  Optional[str]
    pec =  Optional[str]
    telefono =  Optional[str]
    cellulare =  Optional[str]
    fax =  Optional[str]







class AnagrafeBase(SQLModel):
    idanagrafe: int
    nome: str
    cognome: str
    sesso: str  
    cf: str
    note: Optional[str]
    data_nato: Optional[date]
    
    
    via: Optional[str] = Field(sa_column=Column("residenzavia", String, default=None))
    civico: Optional[str] = Field(sa_column=Column("residenzanrciv", String, default=None))
    localita: Optional[str] = Field(sa_column=Column("residenzaloc", String, default=None))
    cap: Optional[str] = Field(sa_column=Column("residenzacap", String, default=None))
    
class Anagrafe(AnagrafeBase, table=True):   
    idanagrafe: Optional[int] = Field(default=None, primary_key=True)
    idcomnasc: Optional[int] = Field(default=None, foreign_key="attivita.ae_comuni.idcomune")
    idcomres: Optional[int] = Field(default=None, foreign_key="attivita.ae_comuni.idcomune")
    comune: "Comune" = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"anagrafe.idcomnasc==comune.idcomune"})
    comune_res: "Comune" = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"anagrafe.idcomres==comune.idcomune"})
    
    
    
