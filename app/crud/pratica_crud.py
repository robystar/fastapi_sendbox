from typing import List, Optional
from app.models.pratica_model import Pratica
from app.models.user_model import User
from app.schemas.pratica_schema import IPraticaCreate, IPraticaUpdate
from app.crud.base_crud import CRUDBase
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDPratica(CRUDBase[Pratica, IPraticaCreate, IPraticaUpdate]):
    async def get_pratica_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Pratica:
        db_session = db_session or db.session
        pratica = await db_session.execute(select(Pratica).where(Pratica.name == name))
        return pratica.scalar_one_or_none()

    async def add_user_to_pratica(self, *, user: User, pratica_id: UUID) -> Pratica:
        pratica = await super().get(id=pratica_id)
        pratica.users.append(user)        
        db.session.add(pratica)
        await db.session.commit()
        await db.session.refresh(pratica)
        return pratica

    async def add_users_to_pratica(self, *, users: List[User], pratica_id: UUID, db_session: Optional[AsyncSession] = None) -> Pratica:
        db_session = db_session or db.session
        pratica = await super().get(id=pratica_id, db_session=db_session)
        pratica.users.extend(users)        
        db_session.add(pratica)
        await db_session.commit()
        await db_session.refresh(pratica)
        return pratica

pratica = CRUDPratica(Pratica)
