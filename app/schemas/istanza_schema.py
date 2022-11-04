from typing import List, Optional
from app.models.istanza_model import IstanzaBase
from uuid import UUID

from app.schemas.soggetto_schema import IRichiedenteRead, IRichiedenteReadAll, IRichiedenteCreateAll, IDelegatoCreate, ITecnicoRead

class IIstanzaCreate(IstanzaBase):
    id: Optional[int]

class IIstanzaCreateAll(IstanzaBase):
    delegato: Optional[IDelegatoCreate]
    richiedenti: List[IRichiedenteCreateAll]

class IIstanzaRead(IstanzaBase):
    id: Optional[int]

class IIstanzaUpdate(IstanzaBase):
    pass

class IIstanzaReadWithRichiedenti(IstanzaBase):
    delegato: Optional[IDelegatoCreate]    
    richiedenti: List[IRichiedenteReadAll]
    tecnici: List[ITecnicoRead]
