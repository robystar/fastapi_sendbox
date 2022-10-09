from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.impresa_model import Impresa
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.impresa_schema import (
    IImpresaCreate,
    IImpresaRead,
    IImpresaUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IResponseBase[Page[IImpresaRead]])
async def get_impresa_list(
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of impresas
    """
    impresas = await crud.impresa.get_multi_paginated(params=params)
    return create_response(data=impresas)


@router.get("/by_created_at", response_model=IResponseBase[Page[IImpresaRead]])
async def get_impresa_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of impresas ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Impresa).order_by(Impresa.created_at.desc())
    else:
        query = select(Impresa).order_by(Impresa.created_at.asc())

    impresas = await crud.impresa.get_multi_paginated(query=query, params=params)
    return create_response(data=impresas)


@router.get("/{impresa_id}", response_model=IGetResponseBase[IImpresaRead])
async def get_Impresa_by_id(
    impresa_id: UUID,
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Impresa by its id
    """
    impresa = await crud.impresa.get(id=impresa_id)
    if not impresa:
        raise HTTPException(status_code=404, detail="Impresa not found")
    return create_response(data=impresa)


@router.post("", response_model=IPostResponseBase[IImpresaRead])
async def create_Impresa(
    impresa: IImpresaCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Impresa
    """
    impresa = await crud.impresa.create(obj_in=impresa, created_by_id=current_user.id)
    return create_response(data=impresa)


@router.put("/{impresa_id}", response_model=IPutResponseBase[IImpresaRead])
async def update_Impresa(
    impresa_id: UUID,
    impresa: IImpresaUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Impresa by its id
    """
    current_impresa = await crud.impresa.get(id=impresa_id)
    if not current_impresa:
        raise HTTPException(status_code=404, detail="Impresa not found")
    impresa_updated = await crud.impresa.update(obj_new=Impresa, obj_current=current_impresa)
    return create_response(data=impresa_updated)


@router.delete("/{impresa_id}", response_model=IDeleteResponseBase[IImpresaRead])
async def remove_Impresa(
    impresa_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Impresa by its id
    """
    current_impresa = await crud.impresa.get(id=impresa_id)
    if not current_impresa:
        raise HTTPException(status_code=404, detail="Impresa not found")
    impresa = await crud.impresa.remove(id=impresa_id)
    return create_response(data=impresa)
