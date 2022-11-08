from typing import List, Optional,Union
from app.models.istanza_model import IstanzaBase
from uuid import UUID
from app.models.ubicazione_model import Civico, Mappale_nceu, Mappale_nct

from app.schemas.soggetto_schema import IDelegatoUpdate, IRichiedenteRead, IRichiedenteReadAll, IRichiedenteCreateAll, IDelegatoCreate, IRichiedenteUpdateAll, ITecnicoRead
from app.schemas.ubicazione_schema import ICivicoRead, IMappaleRead, IPosizioneCreate, IPosizioneRead
from datetime import datetime

class IIstanzaCreate(IstanzaBase):
    id: Optional[int]

class IIstanzaCreateAll(IstanzaBase):
    delegato: Optional[IDelegatoCreate]
    richiedenti: List[IRichiedenteCreateAll]
    
class IIstanzaUpdateAll(IstanzaBase):
    delegato: Optional[IDelegatoUpdate]
    richiedenti: List[IRichiedenteUpdateAll]    
    
class IIstanzaUpdateUbicazione(IstanzaBase):
    id: Optional[int]
    posizione: Optional[IPosizioneCreate]
    

class IIstanzaRead(IstanzaBase):
    id: Optional[int]

class IIstanzaUpdate(IstanzaBase):
    pass

class IIstanzaReadWithRichiedenti(IstanzaBase):
    delegato: Optional[IDelegatoCreate]    
    richiedenti: List[IRichiedenteReadAll]

class IIstanzaReadWithTecnici(IstanzaBase):
    tecnici: List[ITecnicoRead]
    
class IIstanzaReadWithUbicazione(IstanzaBase):
    posizione: Optional[IPosizioneRead]
    civici: List[ICivicoRead]   
    nct: List[IMappaleRead]
    nceu: List[IMappaleRead] 

