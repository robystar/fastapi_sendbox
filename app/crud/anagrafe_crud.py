from typing import Optional
from app.schemas.anagrafe_schema import IAnagrafeCreate, IAnagrafeUpdate
from app.crud.base_crud import CRUDBase
from app.models.anagrafe_model import Anagrafe
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi_pagination import Params, Page

class CRUDAnagrafe(CRUDBase[Anagrafe, IAnagrafeCreate, IAnagrafeUpdate]):
    
    async def get_anagrafe_by_id(self, *, id: int) -> Page[Anagrafe]:
        return await self.get_multi_paginated(query=select(Anagrafe).where(Anagrafe.idanagrafe == id))
    
    async def get_anagrafe_by_cognome(self, *, cognome: str) -> Page[Anagrafe]:
        return await self.get_multi_paginated(query=select(Anagrafe).where(Anagrafe.cognome.startswith(cognome)))

    async def get_anagrafe_by_cf(self, *, cf: str) -> Page[Anagrafe]:
        return await self.get_multi_paginated(query=select(Anagrafe).where(Anagrafe.cf == cf))
        

anagrafe = CRUDAnagrafe(Anagrafe)
