from typing import Optional
from app.models.istanza_model import Asseverazioni, Intervento, Vincoli, IJSONDataCreate
from app.crud.base_crud import CRUDBase
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


class CRUDIntervento(CRUDBase[Intervento, IJSONDataCreate, IJSONDataCreate]):
    pass
    
class CRUDAsseverazioni(CRUDBase[Intervento, IJSONDataCreate, IJSONDataCreate]):
    pass

class CRUDVincoli(CRUDBase[Intervento, IJSONDataCreate, IJSONDataCreate]):
    pass


intervento = CRUDIntervento(Intervento)
asseverazioni = CRUDIntervento(Asseverazioni)
vincoli = CRUDIntervento(Vincoli)
