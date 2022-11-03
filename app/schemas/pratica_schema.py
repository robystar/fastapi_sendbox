from typing import List
from app.models.pratica_model import PraticaBase
from uuid import UUID

class IPraticaCreate(PraticaBase):
    pass

class IPraticaRead(PraticaBase):
    id: int

class IPraticaUpdate(PraticaBase):
    pass
