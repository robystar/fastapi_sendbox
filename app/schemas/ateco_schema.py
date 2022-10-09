from typing import List, Optional
from app.models.ateco_model import AtecoBase
from pydantic import BaseModel

class IAtecoRead(AtecoBase):
    pass

class IAtecoCreate(AtecoBase):
    pass

class IAtecoUpdate(BaseModel):
    pass

class IAtecoReadWithHeroes(IAtecoRead):
    pass

    