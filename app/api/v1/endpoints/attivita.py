from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.attivita_model import Attivita
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.attivita_schema import (
    IAttivitaCreate,
    IAttivitaRead,
    IAttivitaUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IResponseBase[Page[IAttivitaRead]])
async def get_attivita_list(
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of attivitas
    """
    attivita = await crud.attivita.get_multi_paginated(params=params)
    return create_response(data=attivita)


@router.get("/by_created_at", response_model=IResponseBase[Page[IAttivitaRead]])
async def get_attivita_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of attivitas ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Attivita).order_by(Attivita.created_at.desc())
    else:
        query = select(Attivita).order_by(Attivita.created_at.asc())

    attivitas = await crud.attivita.get_multi_paginated(query=query, params=params)
    return create_response(data=attivitas)


@router.get("/{attivita_id}", response_model=IGetResponseBase[IAttivitaRead])
async def get_Attivita_by_id(
    attivita_id: int,
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Attivita by its id
    """
    attivita = await crud.attivita.get_attivita_by_id(id=attivita_id)
    if not attivita:
        raise HTTPException(status_code=404, detail="Attivita not found")
    return create_response(data=attivita)


@router.post("", response_model=IPostResponseBase[IAttivitaRead])
async def create_Attivita(
    attivita: IAttivitaCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Attivita
    """
    attivita = await crud.attivita.create(obj_in=attivita, created_by_id=current_user.id)
    return create_response(data=attivita)


@router.put("/{attivita_id}", response_model=IPutResponseBase[IAttivitaRead])
async def update_Attivita(
    attivita_id: UUID,
    attivita: IAttivitaUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Attivita by its id
    """
    current_attivita = await crud.attivita.get(id=attivita_id)
    if not current_attivita:
        raise HTTPException(status_code=404, detail="Attivita not found")
    attivita_updated = await crud.attivita.update(obj_new=Attivita, obj_current=current_attivita)
    return create_response(data=attivita_updated)


@router.delete("/{attivita_id}", response_model=IDeleteResponseBase[IAttivitaRead])
async def remove_Attivita(
    attivita_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Attivita by its id
    """
    current_attivita = await crud.attivita.get(id=attivita_id)
    if not current_attivita:
        raise HTTPException(status_code=404, detail="Attivita not found")
    attivita = await crud.attivita.remove(id=attivita_id)
    return create_response(data=attivita)
