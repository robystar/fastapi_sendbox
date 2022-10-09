from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.power_model import Power
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.power_schema import (
    IPowerCreate,
    IPowerRead,
    IPowerUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IGetResponseBase[IPowerRead])
async def get_power_list(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of powers
    """
    powers = await crud.power.get_multi_paginated(params=params)
    return create_response(data=powers)


@router.get("/by_created_at", response_model=IResponseBase[Page[IPowerRead]])
async def get_power_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of powers ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Power).order_by(Power.created_at.desc())
    else:
        query = select(Power).order_by(Power.created_at.asc())

    powers = await crud.power.get_multi_paginated(query=query, params=params)
    return create_response(data=powers)


@router.get("/{power_id}", response_model=IGetResponseBase[IPowerRead])
async def get_Power_by_id(
    power_id: UUID,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Power by its id
    """
    power = await crud.power.get(id=power_id)
    if not power:
        raise HTTPException(status_code=404, detail="Power not found")
    return create_response(data=power)


@router.post("", response_model=IPostResponseBase[IPowerRead])
async def create_Power(
    power: IPowerCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Power
    """
    power = await crud.power.create(obj_in=power, created_by_id=current_user.id)
    return create_response(data=power)


@router.put("/{power_id}", response_model=IPutResponseBase[IPowerRead])
async def update_Power(
    power_id: UUID,
    power: IPowerUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Power by its id
    """
    current_power = await crud.power.get(id=power_id)
    if not current_power:
        raise HTTPException(status_code=404, detail="Power not found")
    power_updated = await crud.power.update(obj_new=Power, obj_current=current_power)
    return create_response(data=power_updated)


@router.delete("/{power_id}", response_model=IDeleteResponseBase[IPowerRead])
async def remove_Power(
    power_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Power by its id
    """
    current_power = await crud.power.get(id=power_id)
    if not current_power:
        raise HTTPException(status_code=404, detail="Power not found")
    power = await crud.power.remove(id=power_id)
    return create_response(data=power)
