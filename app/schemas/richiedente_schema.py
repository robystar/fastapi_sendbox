from typing import List, Optional
from app.models.richiedente_model import DomicilioBase, RichiedenteBase, GiuridicaBase, DelegatoBase
from enum import Enum

class ISesso(str, Enum):
    maschile = 'M'
    femminile = 'F'

class IGiuridicaCreate(GiuridicaBase):
    pass
class IGiuridicaRead(GiuridicaBase):
    pass
class IGiuridicaUpdate(GiuridicaBase):
    pass

class IDomicilioCreate(DomicilioBase):
    pass
class IDomicilioRead(DomicilioBase):
    pass
class IDomicilioUpdate(DomicilioBase):
    pass


class IRichiedenteCreate(RichiedenteBase): 
    istanza_id: int

class IRichiedenteCreateAll(RichiedenteBase): 
    domicilio: Optional[IDomicilioCreate]
    giuridica: Optional[IGiuridicaCreate]

class IRichiedenteRead(RichiedenteBase):
    pass
class IRichiedenteReadAll(RichiedenteBase):
    istanza_id: Optional[int]
    domicilio: Optional[IDomicilioRead]
    giuridica: Optional[IGiuridicaRead]
class IRichiedenteUpdate(RichiedenteBase):
    pass

class IDelegatoCreate(DelegatoBase):
    pass
class IDelegatoRead(DelegatoBase):
    pass
class IDelegatoUpdate(DelegatoBase):
    pass

    