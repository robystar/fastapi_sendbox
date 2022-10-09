from typing import Optional,List
from app.schemas.ateco_schema import IAtecoCreate, IAtecoUpdate, IAtecoRead
from app.crud.base_crud import CRUDBase
from app.models.ateco_model import Ateco
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi_pagination.ext.async_sqlalchemy import paginate
from fastapi_pagination import Params, Page


class CRUDAteco(CRUDBase[Ateco, IAtecoCreate, IAtecoUpdate]):
    async def get_ateco_by_codice(self, *, codice: str, db_session: Optional[AsyncSession] = None) -> Page[Ateco]:
        return await self.get_multi_paginated(query=select(Ateco).where(Ateco.codateco.startswith(codice)))

    async def get_ateco_by_categoria(self, *, categoria: str, db_session: Optional[AsyncSession] = None) -> Page[Ateco]:
        return await self.get_multi_paginated(query=select(Ateco).where(Ateco.codcat == categoria))
        
    async def get_ateco_by_descrizione(self, *, desc: str, db_session: Optional[AsyncSession] = None) -> Page[Ateco]:
        return await self.get_multi_paginated(select(Ateco).where(Ateco.catateco.find(desc)!=-1))
    
ateco = CRUDAteco(Ateco)

