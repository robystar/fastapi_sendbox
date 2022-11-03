from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.recipe_model import Ingredient
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.recipe_schema import (
    IIngredientCreate,
    IIngredientRead,
    IIngredientUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IResponseBase[Page[IIngredientRead]])
async def get_ingredient_list(
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of ingredients
    """
    ingredients = await crud.ingredient.get_multi_paginated(params=params)
    return create_response(data=ingredients)


@router.get("/by_created_at", response_model=IResponseBase[Page[IIngredientRead]])
async def get_ingredient_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of ingredients ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Ingredient).order_by(Ingredient.created_at.desc())
    else:
        query = select(Ingredient).order_by(Ingredient.created_at.asc())

    ingredients = await crud.ingredient.get_multi_paginated(query=query, params=params)
    return create_response(data=ingredients)


@router.get("/{ingredient_id}", response_model=IGetResponseBase[IIngredientRead])
async def get_Ingredient_by_id(
    ingredient_id: UUID,
    #current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a Ingredient by its id
    """
    ingredient = await crud.ingredient.get(id=ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return create_response(data=ingredient)


@router.post("", response_model=IPostResponseBase[IIngredientRead])
async def create_Ingredient(
    ingredient: IIngredientCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new Ingredient
    """
    ingredient = await crud.ingredient.create(obj_in=ingredient, created_by_id=current_user.id)
    return create_response(data=ingredient)


@router.put("/{ingredient_id}", response_model=IPutResponseBase[IIngredientRead])
async def update_Ingredient(
    ingredient_id: UUID,
    ingredient: IIngredientUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a Ingredient by its id
    """
    current_ingredient = await crud.ingredient.get(id=ingredient_id)
    if not current_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    ingredient_updated = await crud.ingredient.update(obj_new=Ingredient, obj_current=current_ingredient)
    return create_response(data=ingredient_updated)


@router.delete("/{ingredient_id}", response_model=IDeleteResponseBase[IIngredientRead])
async def remove_Ingredient(
    ingredient_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a Ingredient by its id
    """
    current_ingredient = await crud.ingredient.get(id=ingredient_id)
    if not current_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    ingredient = await crud.ingredient.remove(id=ingredient_id)
    return create_response(data=ingredient)
