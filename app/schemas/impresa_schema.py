from typing import List, Optional
from app.models.impresa_model import ImpresaBase
from pydantic import BaseModel

class IImpresaRead(ImpresaBase):
    id: int

class IImpresaCreate(ImpresaBase):
    pass

class IImpresaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class IImpresaReadWithHeroes(IImpresaRead):
    pass

    