from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import Optional, List

class ComuneBase(SQLModel):
    codiceistat: str = Field(default=None)
    comune: str = Field(default=None)
    provincia: str = Field(default=None)
    siglaprovincia: str = Field(default=None)
    regione: str = Field(default=None)

class Comune(ComuneBase, table=True):   
    __tablename__ = 'ae_comuni'
    __table_args__ = {'schema': 'attivita'}
    idcomune: Optional[int] = Field(default=None, primary_key=True)
