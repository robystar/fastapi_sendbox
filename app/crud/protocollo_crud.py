from typing import Optional
from app.schemas.protocollo_schema import IProtocolloCreate, IProtocolloUpdate
from app.crud.base_crud import CRUDBase
from app.models.protocollo_model import Protocollo
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDProtocollo(CRUDBase[Protocollo, IProtocolloCreate, IProtocolloUpdate]):
    async def get_protocollo_by_numero(self, *, numero: int, db_session: Optional[AsyncSession] = None) -> Protocollo:
        db_session = db_session or db.session
        protocollo = await db_session.execute(select(Protocollo).where(Protocollo.numero_protocollo == numero))
        return protocollo.scalar_one_or_none()

protocollo = CRUDProtocollo(Protocollo)
