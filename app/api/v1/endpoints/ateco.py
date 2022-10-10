from asyncio.log import logger
from typing import Optional, cast, List

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.ateco_model import Ateco
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.ateco_schema import (
    IAtecoCreate,
    IAtecoRead,
    IAtecoUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IResponseBase[Page[IAtecoRead]])
async def get_ateco_list(
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
    codice:str|None=None, categoria:str|None=None, desc:str|None=None
):
    """
    Gets a paginated list of codici ATECO
    """
    query = select(Ateco)

    if codice:
        query = query.where(Ateco.codateco.startswith(codice))
    if categoria:
        query = query.where(Ateco.codcat == categoria)
    if desc:
        query = query.where(Ateco.catateco.ilike('%'+ desc + '%'))

    print(query.compile(compile_kwargs={"literal_binds": True}))
    logger.info("asdasdasd")

    results = await crud.ateco.get_multi_paginated(params=params, query=query)
    return create_response(data=results)


@router.get("/by_created_at", response_model=IResponseBase[Page[IAtecoRead]])
async def get_ateco_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of atecos ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Ateco).order_by(Ateco.created_at.desc())
    else:
        query = select(Ateco).order_by(Ateco.created_at.asc())

    atecos = await crud.ateco.get_multi_paginated(query=query, params=params)
    return create_response(data=atecos)


@router.get("/codice/{codice_ateco}", response_model=IResponseBase[List[IAtecoRead]])
async def get_Ateco_by_id(
    codice_ateco: str
):
    """
    Gets a Ateco by its id
    """
    ateco = await crud.ateco.get_ateco_by_codice(codice=codice_ateco)
    if not ateco:
        raise HTTPException(status_code=404, detail="Ateco not found")
    return create_response(data=ateco)

@router.get("/categoria/{categoria_ateco}", response_model=IResponseBase[Page[IAtecoRead]])
async def get_Ateco_by_categoria(
    categoria_ateco: str
):
    """
    Gets a Ateco by categoria
    """
    ateco = await crud.ateco.get_ateco_by_categoria(categoria=categoria_ateco)
    if not ateco:
        raise HTTPException(status_code=404, detail="Ateco not found")
    return create_response(data=ateco)


@router.post("", response_model=IPostResponseBase[IAtecoRead])
async def create_Ateco(
    ateco: IAtecoCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Ateco
    """
    ateco = await crud.ateco.create(obj_in=ateco, created_by_id=current_user.id)
    return create_response(data=ateco)


@router.put("/{ateco_id}", response_model=IPutResponseBase[IAtecoRead])
async def update_Ateco(
    ateco_id: UUID,
    ateco: IAtecoUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Ateco by its id
    """
    current_ateco = await crud.ateco.get(id=ateco_id)
    if not current_ateco:
        raise HTTPException(status_code=404, detail="Ateco not found")
    ateco_updated = await crud.ateco.update(obj_new=Ateco, obj_current=current_ateco)
    return create_response(data=ateco_updated)


@router.delete("/{ateco_id}", response_model=IDeleteResponseBase[IAtecoRead])
async def remove_Ateco(
    ateco_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Ateco by its id
    """
    current_ateco = await crud.ateco.get(id=ateco_id)
    if not current_ateco:
        raise HTTPException(status_code=404, detail="Ateco not found")
    ateco = await crud.ateco.remove(id=ateco_id)
    return create_response(data=ateco)
