from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.protocollo_model import Protocollo
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.protocollo_schema import (
    IProtocolloCreate,
    IProtocolloRead,
    IProtocolloUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IResponseBase[Page[IProtocolloRead]])
async def get_protocollo_list(
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of protocollos
    """
    protocollos = await crud.protocollo.get_multi_paginated(params=params)
    return create_response(data=protocollos)


@router.get("/by_created_at", response_model=IResponseBase[Page[IProtocolloRead]])
async def get_protocollo_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of protocollos ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Protocollo).order_by(Protocollo.created_at.desc())
    else:
        query = select(Protocollo).order_by(Protocollo.created_at.asc())

    protocollos = await crud.protocollo.get_multi_paginated(query=query, params=params)
    return create_response(data=protocollos)


@router.get("/{protocollo_id}", response_model=IGetResponseBase[IProtocolloRead])
async def get_Protocollo_by_id(
    protocollo_id: UUID,
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Protocollo by its id
    """
    protocollo = await crud.protocollo.get(id=protocollo_id)
    if not protocollo:
        raise HTTPException(status_code=404, detail="Protocollo not found")
    return create_response(data=protocollo)


@router.post("", response_model=IPostResponseBase[IProtocolloRead])
async def create_Protocollo(
    protocollo: IProtocolloCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Protocollo
    """
    protocollo = await crud.protocollo.create(obj_in=protocollo, created_by_id=current_user.id)
    return create_response(data=protocollo)


@router.put("/{protocollo_id}", response_model=IPutResponseBase[IProtocolloRead])
async def update_Protocollo(
    protocollo_id: UUID,
    protocollo: IProtocolloUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Protocollo by its id
    """
    current_protocollo = await crud.protocollo.get(id=protocollo_id)
    if not current_protocollo:
        raise HTTPException(status_code=404, detail="Protocollo not found")
    protocollo_updated = await crud.protocollo.update(obj_new=Protocollo, obj_current=current_protocollo)
    return create_response(data=protocollo_updated)


@router.delete("/{protocollo_id}", response_model=IDeleteResponseBase[IProtocolloRead])
async def remove_Protocollo(
    protocollo_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Protocollo by its id
    """
    current_protocollo = await crud.protocollo.get(id=protocollo_id)
    if not current_protocollo:
        raise HTTPException(status_code=404, detail="Protocollo not found")
    protocollo = await crud.protocollo.remove(id=protocollo_id)
    return create_response(data=protocollo)
