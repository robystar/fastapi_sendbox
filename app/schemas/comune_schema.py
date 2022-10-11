from typing import List, Optional
from app.models.comune_model import ComuneBase
from pydantic import BaseModel

class IComuneRead(ComuneBase):
    idcomune: int

class IComuneCreate(ComuneBase):
    pass

class IComuneUpdate(BaseModel):
    pass


    