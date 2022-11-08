from typing import List, Optional

from sqlmodel import SQLModel
from app.models.ubicazione_model import Civico, CivicoBase, MappaleBase, Mappale_nct, Mappale_nceu, Posizione, PosizioneBase, UbicazioneBase


class IPosizioneCreate(PosizioneBase):
    istanza_id: Optional[int]
    pass

class IPosizioneRead(PosizioneBase):
    pass

class ICivicoCreate(CivicoBase):
    coords: Optional[str]
    
class ICivicoRead(CivicoBase):
    pass
    
class IMappale_nctCreate(MappaleBase):
    geom: Optional[str]
  
class IMappale_nceuCreate(MappaleBase):
    istanza_id: Optional[int]
    subalterno: Optional[str]    
    
class IMappaleRead(MappaleBase):
    pass

class IUbicazioneCreate(SQLModel):
    posizione: IPosizioneCreate
    civici: List[ICivicoCreate]
    nct: List[IMappale_nctCreate]
    nceu: List[IMappale_nceuCreate]
    

class IUbicazioneUpdate(IUbicazioneCreate):
    pass

