from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.anagrafe_model import Anagrafe
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.anagrafe_schema import (
    IAnagrafeCreate,
    IAnagrafeRead,
    IAnagrafeUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IResponseBase[Page[IAnagrafeRead]])
async def get_anagrafe_list(
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of anagrafe
    """
    anagrafe = await crud.anagrafe.get_multi_paginated(params=params)
    return create_response(data=anagrafe)


@router.get("/by_created_at", response_model=IResponseBase[Page[IAnagrafeRead]])
async def get_anagrafe_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of anagrafes ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Anagrafe).order_by(Anagrafe.created_at.desc())
    else:
        query = select(Anagrafe).order_by(Anagrafe.created_at.asc())

    anagrafes = await crud.anagrafe.get_multi_paginated(query=query, params=params)
    return create_response(data=anagrafes)


@router.get("/{anagrafe_id}", response_model=IGetResponseBase[IAnagrafeRead])
async def get_Anagrafe_by_id(
    anagrafe_id: int,
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Anagrafe by its id
    """
    anagrafe = await crud.anagrafe.get_anagrafe_by_id(id=anagrafe_id)
    if not anagrafe:
        raise HTTPException(status_code=404, detail="Anagrafe not found")
    return create_response(data=anagrafe)


@router.post("", response_model=IPostResponseBase[IAnagrafeRead])
async def create_Anagrafe(
    anagrafe: IAnagrafeCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Anagrafe
    """
    anagrafe = await crud.anagrafe.create(obj_in=anagrafe, created_by_id=current_user.id)
    return create_response(data=anagrafe)


@router.put("/{anagrafe_id}", response_model=IPutResponseBase[IAnagrafeRead])
async def update_Anagrafe(
    anagrafe_id: UUID,
    anagrafe: IAnagrafeUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Anagrafe by its id
    """
    current_anagrafe = await crud.anagrafe.get(id=anagrafe_id)
    if not current_anagrafe:
        raise HTTPException(status_code=404, detail="Anagrafe not found")
    anagrafe_updated = await crud.anagrafe.update(obj_new=Anagrafe, obj_current=current_anagrafe)
    return create_response(data=anagrafe_updated)


@router.delete("/{anagrafe_id}", response_model=IDeleteResponseBase[IAnagrafeRead])
async def remove_Anagrafe(
    anagrafe_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Anagrafe by its id
    """
    current_anagrafe = await crud.anagrafe.get(id=anagrafe_id)
    if not current_anagrafe:
        raise HTTPException(status_code=404, detail="Anagrafe not found")
    anagrafe = await crud.anagrafe.remove(id=anagrafe_id)
    return create_response(data=anagrafe)
