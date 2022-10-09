from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import Optional, List

class ImpresaBase(SQLModel):
    idimpresa: int
    ragionesociale: str
    sedevia: str = Field(default=None, title="Sede")
    sedenrc: str = Field( default=None, title="Civico")
    
    
class Impresa(ImpresaBase, table=True):   
    __tablename__ = 'ae_impresa'
    __table_args__ = {'schema': 'attivita'}
    idimpresa: Optional[int] = Field(default=None, primary_key=True)
    idtiposocieta: Optional[int] = Field(default=None, foreign_key="attivita.ae_tipo_societa.idtiposocieta")



