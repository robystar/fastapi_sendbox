from typing import Optional, Union
from app.schemas.soggetto_schema import ITecnicoCreate, ITecnicoUpdate, ITecnicoRead
from app.crud.base_crud import CRUDBase
from app.models.soggetto_model import Tecnico, Domicilio, Giuridica
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDTecnico(CRUDBase[Tecnico, ITecnicoCreate, ITecnicoUpdate]):
    async def get_tecnico_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Tecnico:
        db_session = db_session or db.session
        tecnico = await db_session.execute(select(Tecnico).where(Tecnico.name == name))
        return tecnico.scalar_one_or_none()
     
tecnico = CRUDTecnico(Tecnico)
