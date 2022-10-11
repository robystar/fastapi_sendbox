from typing import List, Optional
from app.models.attivita_model import AttivitaBase
from app.models.impresa_model import ImpresaBase
from app.models.anagrafe_model import AnagrafeBase
from pydantic import BaseModel
from enum import Enum

class IAttivitaRead(AttivitaBase):
    idattivita: int
    impresa: Optional[ImpresaBase]
    anagrafe: Optional[AnagrafeBase]

class IAttivitaCreate(AttivitaBase):
    pass

class IAttivitaUpdate(AttivitaBase):
    idattivita: int
    impresa: Optional[ImpresaBase]
    anagrafe: Optional[AnagrafeBase]
    pass


class IAttivitaStato(str, Enum):
    avviata = 'Avviata'
    cessata = 'Cessata'

    