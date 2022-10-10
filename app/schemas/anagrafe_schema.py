from typing import List, Optional
from app.models.anagrafe_model import AnagrafeBase
from app.models.comune_model import ComuneBase
from pydantic import BaseModel

from app.schemas.comune_schema import IComuneRead

class IAnagrafeRead(AnagrafeBase):
    idanagrafe: str
    comune: Optional[IComuneRead]
    comune_res: Optional[IComuneRead]
    
class IAnagrafeCreate(AnagrafeBase):
    pass

class IAnagrafeUpdate(BaseModel):
    idanagrafe: str
    comune: Optional[IComuneRead]
    comune_res: Optional[IComuneRead]

class IAnagrafeReadWithHeroes(IAnagrafeRead):
    pass

    