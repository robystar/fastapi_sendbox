from app.models.user_model import User
from app.schemas.common_schema import (
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.soggetto_schema import (
    ITecnicoCreate,
    ITecnicoRead,
    ITecnicoUpdate
)
from fastapi import APIRouter, Depends, HTTPException, Body
from app.api import deps
from app import crud
from uuid import UUID
from app.schemas.soggetto_schema import ITecnicoRuolo
from app.schemas.role_schema import IRoleEnum

from .examples import tecnico, tecnici

router = APIRouter()


@router.get("", response_model=IGetResponseBase[Page[ITecnicoRead]])
async def get_tecnici(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of tecnicos
    """
    tecnici = await crud.tecnico.get_multi_paginated(params=params)
    return create_response(data=tecnici)


@router.get("/{tecnico_id}", response_model=IGetResponseBase[ITecnicoRead])
async def get_tecnico_by_id(
    tecnico_id: int,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a tecnico by its id
    """
    tecnico = await crud.tecnico.get(id=tecnico_id)
    return create_response(data=tecnico)


@router.post("", response_model=IPostResponseBase[ITecnicoRead])
async def create_tecnico(
    tecnico: ITecnicoCreate = Body(
        example=tecnico,
    ),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new tecnico
    """
    new_tecnico = await crud.tecnico.create(obj_in=tecnico)
    return create_response(data=new_tecnico)


@router.put("/{tecnico_id}", response_model=IPutResponseBase[ITecnicoRead])
async def update_tecnico(
    tecnico_id: int,
    tecnico: ITecnicoUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a tecnico by its id
    """
    tecnico_current = await crud.tecnico.get(id=tecnico_id)
    if not tecnico_current:
        raise HTTPException(status_code=404, detail="Tecnico not found")

    tecnico_updated = await crud.tecnico.update(obj_current=tecnico_current, obj_new=tecnico)
    return create_response(data=tecnico_updated)


