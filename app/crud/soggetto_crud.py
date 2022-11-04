from typing import Optional, Union
from app.schemas.soggetto_schema import IRichiedenteCreate, IRichiedenteUpdate, IRichiedenteReadAll
from app.crud.base_crud import CRUDBase
from app.models.soggetto_model import Richiedente, Domicilio, Giuridica
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDRichiedente(CRUDBase[Richiedente, IRichiedenteCreate, IRichiedenteUpdate]):
    async def get_richiedente_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Richiedente:
        db_session = db_session or db.session
        richiedente = await db_session.execute(select(Richiedente).where(Richiedente.name == name))
        return richiedente.scalar_one_or_none()
     
    async def create(
        self,
        *,
        obj_in: Union[IRichiedenteCreate, Richiedente],
        db_session: Optional[AsyncSession] = None,
    ) -> IRichiedenteReadAll:
        db_session = db_session or db.session
        db_richiedente = Richiedente.from_orm(obj_in)  # type: ignore
        db_richiedente.domicilio = Domicilio.from_orm(obj_in.domicilio)
        db_richiedente.giuridica = Giuridica.from_orm(obj_in.giuridica)
        db_session.add(db_richiedente)
        await db_session.commit()
        await db_session.refresh(db_richiedente)
        return db_richiedente
    
richiedente = CRUDRichiedente(Richiedente)
