from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import Optional, List
from sqlalchemy import Column, String, Integer
from datetime import datetime, date

class AttivitaBase(SQLModel):
    insegna: Optional[str]
    tipoattivita: Optional[str]
    idtipoattivita: Optional[int]
    subattivita: Optional[str]
    idsubattivita: Optional[int]
    specifica: Optional[str]
    idspecifica: Optional[int]
    causale: Optional[str]
    stato: Optional[str]
    data_inizio_attivita: Optional[date]
    data_fine_attivita: Optional[date]
    via: Optional[str]
    civico: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    mq_totali: Optional[float]
    attocessazione: Optional[str]
    noteattiv: Optional[str]
    sup_attiv: Optional[float]
    sup_vendita: Optional[float]
    sup_alimentare: Optional[float]
    sup_mista: Optional[float]
    nr_stelle: Optional[int]
    nr_camere: Optional[int]
    nr_postiletto: Optional[int]
    nr_postiletto_agg: Optional[int]
    nr_uiabit: Optional[int]
    data_presentazione_scia: Optional[date]
    data_scadenza_scia: Optional[date]
    ruolo: Optional[str]


class Attivita(AttivitaBase, table=True):   
    __tablename__ = 'vista_attivita'
    __table_args__ = {'schema': 'attivita'}
    idattivita: Optional[int] = Field(default=None, primary_key=True)
    idanagrafe: Optional[int] = Field(default=None, foreign_key="attivita.ae_anagrafe.idanagrafe")
    anagrafe: Optional["Anagrafe"] = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"Attivita.idanagrafe==Anagrafe.idanagrafe"})
    idimpresa: Optional[int] = Field(default=None, foreign_key="attivita.vista_impresa.idimpresa")
    impresa: Optional["Impresa"] = Relationship(sa_relationship_kwargs={"lazy":"joined", "primaryjoin":"Attivita.idimpresa==Impresa.idimpresa"})
    


    #idruolo: Optional[int] = Field(default=None, foreign_key="attivita.ae_tipo_ruolo.idtiporuolo")
    #idspecifica: Optional[int] = Field(default=None, foreign_key="attivita.ae_specifica.idspecifica")

    
    


