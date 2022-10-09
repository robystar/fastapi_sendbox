from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.weapon_model import Weapon
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.weapon_schema import (
    IWeaponCreate,
    IWeaponRead,
    IWeaponUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IGetResponseBase[IWeaponRead])
async def get_weapon_list(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of Weapones
    """
    weapons = await crud.weapon.get_multi_paginated(params=params)
    return create_response(data=weapons)


@router.get("/by_created_at", response_model=IResponseBase[Page[IWeaponRead]])
async def get_weapon_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of Weapones ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Weapon).order_by(Weapon.created_at.desc())
    else:
        query = select(Weapon).order_by(Weapon.created_at.asc())

    weapons = await crud.weapon.get_multi_paginated(query=query, params=params)
    return create_response(data=weapons)


@router.get("/{weapon_id}", response_model=IGetResponseBase[IWeaponRead])
async def get_weapon_by_id(
    Weapon_id: UUID,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Weapon by its id
    """
    weapon = await crud.weapon.get(id=weapon_id)
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return create_response(data=Weapon)


@router.post("", response_model=IPostResponseBase[IWeaponRead])
async def create_weapon(
    weapon: IWeaponCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Weapon
    """
    weapon = await crud.weapon.create(obj_in=weapon, created_by_id=current_user.id)
    return create_response(data=weapon)


@router.put("/{weapon_id}", response_model=IPutResponseBase[IWeaponRead])
async def update_weapon(
    weapon_id: UUID,
    weapon: IWeaponUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Weapon by its id
    """
    current_weapon = await crud.weapon.get(id=weapon_id)
    if not current_weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    weapon_updated = await crud.weapon.update(obj_new=Weapon, obj_current=current_weapon)
    return create_response(data=weapon_updated)


@router.delete("/{weapon_id}", response_model=IDeleteResponseBase[IWeaponRead])
async def remove_weapon(
    weapon_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Weapon by its id
    """
    current_weapon = await crud.weapon.get(id=weapon_id)
    if not current_weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    weapon = await crud.weapon.remove(id=weapon_id)
    return create_response(data=weapon)
