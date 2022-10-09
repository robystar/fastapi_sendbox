from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import Optional, List
from sqlalchemy import Column, String, Integer

class AttivitaBase(SQLModel):
    insegna: str


class Attivita(AttivitaBase, table=True):   
    __tablename__ = 'ae_attivita'
    __table_args__ = {'schema': 'attivita'}
    idattivita: Optional[int] = Field(default=None, primary_key=True)
    
    idimpresa: Optional[int] = Field(default=None, foreign_key="attivita.ae_impresa.idimpresa")
    impresa: "Impresa" = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"Attivita.idimpresa==Impresa.idimpresa"})
    
    idanagrafe: Optional[int] = Field(default=None, foreign_key="attivita.ae_anagrafe.idanagrafe")
    anagrafe: "Anagrafe" = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"Attivita.idanagrafe==Anagrafe.idanagrafe"})

    #idruolo: Optional[int] = Field(default=None, foreign_key="attivita.ae_tipo_ruolo.idtiporuolo")
    #idspecifica: Optional[int] = Field(default=None, foreign_key="attivita.ae_specifica.idspecifica")

    
    


