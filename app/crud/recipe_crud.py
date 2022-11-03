from typing import List, Optional
from app.models.recipe_model import Recipe, Ingredient
from app.schemas.recipe_schema import IRecipeCreate, IRecipeUpdate, IIngredientCreate, IIngredientUpdate
from app.crud.base_crud import CRUDBase
from fastapi_async_sqlalchemy import db
from sqlmodel import select
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession

class CRUDRecipe(CRUDBase[Recipe, IRecipeCreate, IRecipeUpdate]):
    async def get_recipe_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Recipe:
        db_session = db_session or db.session
        recipe = await db_session.execute(select(Recipe).where(Recipe.name == name))
        return recipe.scalar_one_or_none()

    async def add_ingredient_to_recipe(self, *, ingredient: Ingredient, recipe_id: UUID) -> Recipe:
        recipe = await super().get(id=recipe_id)
        recipe.ingredients.append(ingredient)        
        db.session.add(recipe)
        await db.session.commit()
        await db.session.refresh(recipe)
        return recipe

    async def add_ingredients_to_group(self, *, ingredients: List[Ingredient], recipe_id: UUID, db_session: Optional[AsyncSession] = None) -> Recipe:
        db_session = db_session or db.session
        recipe = await super().get(id=recipe_id, db_session=db_session)
        recipe.ingredients.extend(ingredients)        
        db_session.add(recipe)
        await db_session.commit()
        await db_session.refresh(recipe)
        return recipe

recipe = CRUDRecipe(Recipe)


class CRUDIngredient(CRUDBase[Ingredient, IIngredientCreate, IIngredientUpdate]):
    async def get_ingredient_by_name(self, *, name: str, db_session: Optional[AsyncSession] = None) -> Ingredient:
        db_session = db_session or db.session
        ingredient = await db_session.execute(select(Ingredient).where(Ingredient.name == name))
        return ingredient.scalar_one_or_none()

ingredient = CRUDIngredient(Ingredient)

