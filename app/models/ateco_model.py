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
    idateco: Optional[int] = Field(default=None, primary_key=True)
