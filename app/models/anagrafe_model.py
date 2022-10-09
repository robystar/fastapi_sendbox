from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from sqlalchemy import Column, String
from typing import Optional, List

class AnagrafeBase(SQLModel):
    nome: str
    cognome: str
    sesso: str  
    cf: str
    note: Optional[str]
    
    
    residenza_via: Optional[str] = Field(sa_column=Column("residenzavia", String, default=None))
    residenza_civico: Optional[str] = Field(sa_column=Column("residenzanrciv", String, default=None))
    residenza_localita: Optional[str] = Field(sa_column=Column("residenzaloc", String, default=None))
    residenza_cap: Optional[str] = Field(sa_column=Column("residenzacap", String, default=None))
    
class Anagrafe(AnagrafeBase, table=True):   
    __tablename__ = 'ae_anagrafe'
    __table_args__ = {'schema': 'attivita'}
    idanagrafe: Optional[int] = Field(default=None, primary_key=True)
    idcomnasc: Optional[int] = Field(default=None, foreign_key="attivita.ae_comuni.idcomune")
    idcomres: Optional[int] = Field(default=None, foreign_key="attivita.ae_comuni.idcomune")
    comune: "Comune" = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"Anagrafe.idcomnasc==Comune.idcomune"})
    residenza_comune: "Comune" = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"Anagrafe.idcomres==Comune.idcomune"})


