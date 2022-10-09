from fastapi import APIRouter
from app.api.v1.endpoints import user, attivita, impresa, anagrafe, comune, ateco, hero, team, power, weapon, login, role, group, cache

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])

api_router.include_router(ateco.router, prefix="/ateco", tags=["Codici ATECO"])

api_router.include_router(attivita.router, prefix="/attivita", tags=["Attività"])
api_router.include_router(impresa.router, prefix="/impresa", tags=["Imprese"])
api_router.include_router(anagrafe.router, prefix="/anagrafe", tags=["Anagrafe"])
api_router.include_router(comune.router, prefix="/comuni", tags=["Comuni"])


api_router.include_router(role.router, prefix="/role", tags=["role"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(group.router, prefix="/group", tags=["group"])
api_router.include_router(team.router, prefix="/team", tags=["team"])
api_router.include_router(hero.router, prefix="/hero", tags=["hero"])
api_router.include_router(power.router, prefix="/power", tags=["power"])
api_router.include_router(weapon.router, prefix="/weapon", tags=["weapon"])
api_router.include_router(cache.router, prefix="/cache", tags=["cache"])
