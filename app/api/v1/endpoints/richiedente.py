from app.models.user_model import User
from app.schemas.common_schema import (
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.soggetto_schema import (
    IRichiedenteCreate,
    IRichiedenteRead,
    IRichiedenteReadAll,
    IRichiedenteUpdate
)
from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum

router = APIRouter()


@router.get("", response_model=IGetResponseBase[Page[IRichiedenteReadAll]])
async def get_richiedenti(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of richiedentes
    """
    richiedenti = await crud.richiedente.get_multi_paginated(params=params)
    return create_response(data=richiedenti)


@router.get("/{richiedente_id}", response_model=IGetResponseBase[IRichiedenteReadAll])
async def get_richiedente_by_id(
    richiedente_id: int,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a richiedente by its id
    """
    richiedente = await crud.richiedente.get(id=richiedente_id)
    return create_response(data=richiedente)


@router.post("", response_model=IPostResponseBase[IRichiedenteReadAll])
async def create_richiedente(
    richiedente: IRichiedenteCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new richiedente
    """
    new_richiedente = await crud.richiedente.create(obj_in=richiedente)
    return create_response(data=new_richiedente)


@router.put("/{richiedente_id}", response_model=IPutResponseBase[IRichiedenteRead])
async def update_richiedente(
    richiedente_id: int,
    richiedente: IRichiedenteUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a richiedente by its id
    """
    richiedente_current = await crud.richiedente.get(id=richiedente_id)
    if not richiedente_current:
        raise HTTPException(status_code=404, detail="Richiedente not found")

    richiedente_updated = await crud.richiedente.update(obj_current=richiedente_current, obj_new=richiedente)
    return create_response(data=richiedente_updated)


@router.post(
    "/add_richiedente/{richiedente_id}/{istanza_id}", response_model=IPostResponseBase[IRichiedenteRead]
)
async def add_ingredient_into_a_richiedente(
    istanza_id: int,
    richiedente_id: int,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Adds a ingredient into a richiedente
    """
    ingredient = await crud.ingredient.get(id=ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    richiedente = await crud.richiedente.add_ingredient_to_richiedente(ingredient=ingredient, richiedente_id=richiedente_id)
    return create_response(message="Ingredient added to richiedente", data=richiedente)
