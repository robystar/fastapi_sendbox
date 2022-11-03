from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from typing import Optional, List

class ImpresaBase(SQLModel):
    idimpresa: int
    ragionesociale: Optional[str]
    tiposocieta: Optional[str]
    sedevia: Optional[str]
    sedenrc: Optional[str]
    sedecomune: Optional[str]
    sedeprovincia: Optional[str]
    sedesiglaprov: Optional[str]
    sedeloc: Optional[str]
    sedecap: Optional[str]
    cf_soc: Optional[str]
    piva_soc: Optional[str]
    nr_telfisso: Optional[str]
    nr_telmobile: Optional[str]
    nr_fax: Optional[str]
    email01_soc: Optional[str]
    email02_soc: Optional[str]
    aa_costr: Optional[str]
    dt_rec: Optional[str]
    reg_imprese: Optional[str]
    rea: Optional[str]

class Impresa(ImpresaBase, table=True):   
    idimpresa: Optional[int] = Field(default=None, primary_key=True)


