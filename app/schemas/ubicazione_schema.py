from typing import List, Optional

from sqlmodel import SQLModel
from app.models.ubicazione_model import Civico, CivicoBase, MappaleBase, Mappale_nct, Mappale_nceu, Posizione, PosizioneBase, UbicazioneBase


class IPosizioneCreate(PosizioneBase):
    istanza_id: Optional[int]
    pass
 

class ICivicoCreate(CivicoBase):
    geom_p: Optional[str] 
    
class ICivicoRead(CivicoBase):
    pass
    
class IMappale_nctCreate(MappaleBase):
    geom_plg: Optional[str]
  
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


class IUbicazioneRead(PosizioneBase):
    posizione: IPosizioneCreate
    civici: List[ICivicoCreate]
    nct: List[IMappale_nctCreate]
    nceu: List[IMappale_nceuCreate]   