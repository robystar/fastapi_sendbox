from typing import List, Optional
from app.models.soggetto_model import DomicilioBase, RichiedenteBase, GiuridicaBase, DelegatoBase, TecnicoBase
from enum import Enum

class ISesso(str, Enum):
    maschile = 'M'
    femminile = 'F'

class ITecnicoRuolo(str, Enum):
    progettista = 'progettista'
    progettista_strutt = 'progettista_strutt'
    accertamento = 'accertamento'
    appaltatore = 'appaltatore'
    verificatore = 'verificatore'
    certificatore = 'certificatore'
    direttore = 'direttore'
    direttore_strutt = 'direttore_strutt'
    resp_sicurezza = 'resp_sicurezza'
    collaudatore = 'collaudatore'
    esecutore = 'esecutore'
    geologo = 'geologo'
    tecnico_ca = 'tecnico_ca'
    altro = 'altro'
    
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
    istanza_id: Optional[int]

class IRichiedenteCreateAll(RichiedenteBase): 
    istanza_id: Optional[int]
    domicilio: Optional[IDomicilioCreate]
    giuridica: Optional[IGiuridicaCreate]
    
    
class IRichiedenteUpdateAll(RichiedenteBase): 
    istanza_id: Optional[int]
    domicilio: Optional[IDomicilioUpdate]
    giuridica: Optional[IGiuridicaUpdate]    
    

class IRichiedenteRead(RichiedenteBase):
    pass
class IRichiedenteReadAll(RichiedenteBase):
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

class ITecnicoCreate(TecnicoBase):
    istanza_id: Optional[int]
    pass
class ITecnicoRead(TecnicoBase):
    pass
class ITecnicoUpdate(TecnicoBase):
    pass
    