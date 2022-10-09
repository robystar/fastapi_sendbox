from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.comune_model import Comune
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.comune_schema import (
    IComuneCreate,
    IComuneRead,
    IComuneUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IResponseBase[Page[IComuneRead]])
async def get_comune_list(
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of comunes
    """
    comunes = await crud.comune.get_multi_paginated(params=params)
    return create_response(data=comunes)


@router.get("/by_created_at", response_model=IResponseBase[Page[IComuneRead]])
async def get_comune_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of comunes ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Comune).order_by(Comune.created_at.desc())
    else:
        query = select(Comune).order_by(Comune.created_at.asc())

    comunes = await crud.comune.get_multi_paginated(query=query, params=params)
    return create_response(data=comunes)


@router.get("/{comune_id}", response_model=IGetResponseBase[IComuneRead])
async def get_Comune_by_id(
    comune_id: UUID,
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Comune by its id
    """
    comune = await crud.comune.get(id=comune_id)
    if not comune:
        raise HTTPException(status_code=404, detail="Comune not found")
    return create_response(data=comune)


@router.post("", response_model=IPostResponseBase[IComuneRead])
async def create_Comune(
    comune: IComuneCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Comune
    """
    comune = await crud.comune.create(obj_in=comune, created_by_id=current_user.id)
    return create_response(data=comune)


@router.put("/{comune_id}", response_model=IPutResponseBase[IComuneRead])
async def update_Comune(
    comune_id: UUID,
    comune: IComuneUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Comune by its id
    """
    current_comune = await crud.comune.get(id=comune_id)
    if not current_comune:
        raise HTTPException(status_code=404, detail="Comune not found")
    comune_updated = await crud.comune.update(obj_new=Comune, obj_current=current_comune)
    return create_response(data=comune_updated)


@router.delete("/{comune_id}", response_model=IDeleteResponseBase[IComuneRead])
async def remove_Comune(
    comune_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Comune by its id
    """
    current_comune = await crud.comune.get(id=comune_id)
    if not current_comune:
        raise HTTPException(status_code=404, detail="Comune not found")
    comune = await crud.comune.remove(id=comune_id)
    return create_response(data=comune)
