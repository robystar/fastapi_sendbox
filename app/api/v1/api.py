from fastapi import APIRouter
from app.api.v1.endpoints import ingredient, user, login, role, group, recipe, protocollo, pratica, istanza, richiedente, tecnico, cache

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(istanza.router, prefix="/istanze", tags=["Istanze"])

api_router.include_router(protocollo.router, prefix="/protocollo", tags=["Protocollo"])
api_router.include_router(pratica.router, prefix="/pratiche", tags=["Pratiche"])
api_router.include_router(richiedente.router, prefix="/richiedenti", tags=["Richiedenti"])
api_router.include_router(tecnico.router, prefix="/tecnici", tags=["Tecnici"])

api_router.include_router(recipe.router, prefix="/recipe", tags=["Ricette"])
api_router.include_router(ingredient.router, prefix="/ingredient", tags=["Ingredienti"])

api_router.include_router(role.router, prefix="/role", tags=["Ruoli"])
api_router.include_router(user.router, prefix="/user", tags=["Utenti"])
api_router.include_router(group.router, prefix="/group", tags=["Gruppi"])
api_router.include_router(cache.router, prefix="/cache", tags=["cache"])
