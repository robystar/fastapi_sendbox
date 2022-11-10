from sqlmodel import SQLModel, Field, Relationship, JSON, ForeignKey, Column
from typing import Optional, List
from geoalchemy2 import Geometry

class Via(SQLModel, table=True):   
    __table_args__ = {'schema': 'civici'}
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
 
class CivicoBase(SQLModel): 
    via_id : int
    civico: str
    interno: Optional[str]
    note: Optional[str]

class MappaleBase(SQLModel):
    sezione: Optional[str]
    foglio: str
    mappale: str
    note: Optional[str]
    
class UiuBase(MappaleBase, CivicoBase):
    subaterno: Optional[str]
    interno: Optional[str]
    scala: Optional[str]
    piano: Optional[str]
    vani: Optional[str]
    supeficie: Optional[float]
    destuso: Optional[str]


class PosizioneBase(SQLModel):
    localita: Optional[str]
    note: Optional[str]
    coord_lng: Optional[float]
    coord_lat: Optional[float]
    coord_x: Optional[float]
    coord_y: Optional[float]
    
class UbicazioneBase(SQLModel):
    localita: Optional[str]
    note: Optional[str]
    coord_lng: Optional[float]
    coord_lat: Optional[float]
    coord_x: Optional[float]
    coord_y: Optional[float]    
    

class Civico(CivicoBase, table=True):   
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), nullable=False, default=None))
    via_id: Optional[int] = Field(default=None, nullable=False, foreign_key="civici.via.id")
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    geom_p: Optional[str] = Field(sa_column=Column(Geometry(geometry_type='POINT', srid=4326, spatial_index=True)))
    sostituito: Optional[bool] = Field(default=False)
    class Config:
        arbitrary_types_allowed = True
                
class Mappale_nct(MappaleBase, table=True):   
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), nullable=False, default=None))
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    geom_plg: Optional[str] = Field(sa_column=Column(Geometry(geometry_type='POLYGON', srid=4326, spatial_index=True)))
    sostituito: Optional[bool] = Field(default=False)
    class Config:
        arbitrary_types_allowed = True
          
class Mappale_nceu(MappaleBase, table=True):   
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    subaterno: Optional[str]
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), nullable=False, default=None))
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    sostituito: Optional[bool] = Field(default=False)
 
class Uiu(UiuBase, table=True):
    __table_args__ = {'schema': 'edilizia'}
    id: Optional[int] = Field(default=None, primary_key=True)
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), nullable=False, default=None))
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    sostituito: Optional[bool] = Field(default=False)

class Posizione(PosizioneBase, table=True):
    __table_args__ = {'schema': 'edilizia'}
    istanza_id: Optional[int] = Field(sa_column=Column(ForeignKey("edilizia.istanza.id", ondelete="CASCADE"), primary_key=True, nullable=False, default=None))
    istanza: Optional["Istanza"] = Relationship(sa_relationship_kwargs={"lazy":"selectin"})
    