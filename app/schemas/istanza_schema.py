from typing import List, Optional
from app.models.istanza_model import IstanzaBase
from uuid import UUID

from app.schemas.richiedente_schema import IRichiedenteRead, IRichiedenteReadAll, IRichiedenteCreateAll, IDelegatoCreate

class IIstanzaCreate(IstanzaBase):
    id: Optional[int]

class IIstanzaCreateAll(IstanzaBase):
    richiedenti: List[IRichiedenteCreateAll]
    delegato: Optional[IDelegatoCreate]

class IIstanzaRead(IstanzaBase):
    id: Optional[int]

class IIstanzaUpdate(IstanzaBase):
    pass

class IIstanzaReadWithRichiedenti(IstanzaBase):
    richiedenti: List[IRichiedenteReadAll]
    

