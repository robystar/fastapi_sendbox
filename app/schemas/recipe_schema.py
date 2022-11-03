from typing import List
from app.models.recipe_model import RecipeBase, IngredientBase
from uuid import UUID

class IIngredientCreate(IngredientBase):
    pass

class IIngredientRead(IngredientBase):
    id: UUID

class IIngredientUpdate(IngredientBase):
    pass

class IRecipeCreate(RecipeBase):
    pass

class IRecipeRead(RecipeBase):
    id: UUID

class IRecipeReadWithIngredients(RecipeBase):
    id: UUID
    ingredients: List[IIngredientRead]

class IRecipeUpdate(RecipeBase):
    pass

