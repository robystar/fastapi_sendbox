from typing import Optional
from app.schemas.impresa_schema import IImpresaCreate, IImpresaUpdate
from app.crud.base_crud import CRUDBase
from app.models.impresa_model import Impresa
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDImpresa(CRUDBase[Impresa, IImpresaCreate, IImpresaUpdate]):
    async def get_impresa_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Impresa:
        db_session = db_session or db.session
        impresa = await db_session.execute(select(Impresa).where(Impresa.name == name))
        return impresa.scalar_one_or_none()

impresa = CRUDImpresa(Impresa)
