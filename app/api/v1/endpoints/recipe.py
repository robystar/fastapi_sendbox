from app.models.user_model import User
from app.schemas.common_schema import (
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.recipe_schema import (
    IRecipeCreate,
    IRecipeRead,
    IRecipeReadWithIngredients,
    IRecipeUpdate,
    IRecipeReadWithIngredients,
)
from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum

router = APIRouter()


@router.get("", response_model=IGetResponseBase[Page[IRecipeReadWithIngredients]])
async def get_recipes(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of recipes
    """
    recipes = await crud.recipe.get_multi_paginated(params=params)
    return create_response(data=recipes)


@router.get("/{recipe_id}", response_model=IGetResponseBase[IRecipeReadWithIngredients])
async def get_recipe_by_id(
    recipe_id: UUID,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a recipe by its id
    """
    recipe = await crud.recipe.get(id=recipe_id)
    return create_response(data=recipe)


@router.post("", response_model=IPostResponseBase[IRecipeRead])
async def create_recipe(
    recipe: IRecipeCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new recipe
    """
    new_recipe = await crud.recipe.create(obj_in=recipe, created_by_id=current_user.id)
    return create_response(data=new_recipe)


@router.put("/{recipe_id}", response_model=IPutResponseBase[IRecipeRead])
async def update_recipe(
    recipe_id: UUID,
    recipe: IRecipeUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a recipe by its id
    """
    recipe_current = await crud.recipe.get(id=recipe_id)
    if not recipe_current:
        raise HTTPException(status_code=404, detail="Recipe not found")

    recipe_updated = await crud.recipe.update(obj_current=recipe_current, obj_new=recipe)
    return create_response(data=recipe_updated)


@router.post(
    "/add_ingredient/{ingredient_id}/{recipe_id}", response_model=IPostResponseBase[IRecipeRead]
)
async def add_ingredient_into_a_recipe(
    ingredient_id: UUID,
    recipe_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Adds a ingredient into a recipe
    """
    ingredient = await crud.ingredient.get(id=ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    recipe = await crud.recipe.add_ingredient_to_recipe(ingredient=ingredient, recipe_id=recipe_id)
    return create_response(message="Ingredient added to recipe", data=recipe)
