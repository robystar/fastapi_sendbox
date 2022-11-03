from typing import List, Optional
from app.models.istanza_model import IstanzaBase
from uuid import UUID

from app.schemas.richiedente_schema import IRichiedenteRead, IRichiedenteReadAll

class IIstanzaCreate(IstanzaBase):
    id: Optional[int]
    pass

class IIstanzaRead(IstanzaBase):
    id: Optional[int]

class IIstanzaUpdate(IstanzaBase):
    pass

class IIstanzaReadWithRichiedenti(IstanzaBase):
    richiedenti: List[IRichiedenteReadAll]
    

