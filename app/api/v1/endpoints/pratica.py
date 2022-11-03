from email.policy import strict
from app.models.user_model import User
from app.schemas.common_schema import (
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.pratica_schema import (
    IPraticaCreate,
    IPraticaRead,
    IPraticaUpdate,
)
from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum

router = APIRouter()


@router.get("", response_model=IGetResponseBase[Page[IPraticaRead]])
async def get_praticas(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of praticas
    """
    praticas = await crud.pratica.get_multi_paginated(params=params)
    return create_response(data=praticas)


@router.get("/{pratica_id}", response_model=IGetResponseBase[IPraticaRead])
async def get_pratica_by_id(
    pratica_id: UUID,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a pratica by its id
    """
    pratica = await crud.pratica.get(id=pratica_id)
    return create_response(data=pratica)


@router.post("", response_model=IPostResponseBase[IPraticaRead])
async def create_pratica(
    pratica: IPraticaCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new pratica
    """
    new_pratica = await crud.pratica.create(obj_in=pratica, created_by_id=current_user.id)
    return create_response(data=new_pratica)


@router.put("/{pratica_id}", response_model=IPutResponseBase[IPraticaRead])
async def update_pratica(
    pratica_id: UUID,
    pratica: IPraticaUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a pratica by its id
    """
    pratica_current = await crud.pratica.get(id=pratica_id)
    if not pratica_current:
        raise HTTPException(status_code=404, detail="Pratica not found")

    pratica_updated = await crud.pratica.update(obj_current=pratica_current, obj_new=pratica)
    return create_response(data=pratica_updated)


@router.post(
    "/add_user/{user_id}/{pratica_id}", response_model=IPostResponseBase[IPraticaRead]
)
async def add_user_into_a_pratica(
    user_id: UUID,
    pratica_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Adds a user into a pratica
    """
    user = await crud.user.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    pratica = await crud.pratica.add_user_to_pratica(user=user, pratica_id=pratica_id)
    return create_response(message="User added to pratica", data=pratica)


@router.post(
    "/{db_id}/{doc_id}/{form_id}", response_model=IPostResponseBase[IPraticaRead]
)
async def add_user_into_a_pratica(
    db_id: str,
    doc_id: str,
    form_id: str,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager, IRoleEnum.user])
    ),
):
    """
    posta i dati di salvataggio con form di plomino
    """
    user = await crud.user.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    pratica = await crud.pratica.add_user_to_pratica(user=user, pratica_id=pratica_id)
    return create_response(message="User added to pratica", data=pratica)
