from typing import List, Optional
from app.models.protocollo_model import ProtocolloBase
from pydantic import BaseModel

class IProtocolloRead(ProtocolloBase):
    numero_protocollo: int

class IProtocolloCreate(ProtocolloBase):
    pass

class IProtocolloUpdate(BaseModel):
    pass


    