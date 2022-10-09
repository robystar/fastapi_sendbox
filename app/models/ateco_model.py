from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import Optional, List

class AtecoBase(SQLModel):
    codateco: str = Field(default=None)
    catateco: str = Field(default=None)
    codcat: str = Field(default=None)
    cat: str = Field(default=None)
    codsottocat: str = Field(default=None)
    sottocat: str = Field(default=None)

class Ateco(AtecoBase, table=True):   
    __tablename__ = 'ae_ateco'
    __table_args__ = {'schema': 'attivita'}
    idateco: Optional[int] = Field(default=None, primary_key=True)
