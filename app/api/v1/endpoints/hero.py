from typing import Optional, cast

from app.schemas.common_schema import IResponseBase
from app.models.user_model import User
from app.models.hero_model import Hero
from app.schemas.common_schema import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.hero_schema import (
    IHeroCreate,
    IHeroRead,
    IHeroReadWithPowers,
    IHeroReadWithPowersAndTeam,
    IHeroReadWithTeams,
    IHeroUpdate,
    IHeroCreateWithPowersAndTeams,
    IHeroReadWithPowersAndTeam
)
from fastapi import APIRouter, Depends, HTTPException, Query
from app.api import deps
from sqlmodel import select
from app import crud
from uuid import UUID
from app.schemas.role_schema import IRoleEnum
from app.schemas.common_schema import IOrderEnum

router = APIRouter()


@router.get("", response_model=IGetResponseBase[Page[IHeroReadWithTeams]])
async def get_hero_list(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of heroes
    """
    heroes = await crud.hero.get_multi_paginated(params=params)
    return create_response(data=heroes)


@router.get("/by_created_at", response_model=IResponseBase[Page[IHeroReadWithTeams]])
async def get_hero_list_order_by_created_at(
    order: Optional[IOrderEnum] = Query(
        default=IOrderEnum.ascendent, description="It is optional. Default is ascendent"
    ),
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of heroes ordered by created at datetime
    """
    if order == IOrderEnum.descendent:
        query = select(Hero).order_by(Hero.created_at.desc())
    else:
        query = select(Hero).order_by(Hero.created_at.asc())

    heroes = await crud.hero.get_multi_paginated(query=query, params=params)
    return create_response(data=heroes)


@router.get("/{hero_id}", response_model=IGetResponseBase[IHeroReadWithTeams])
async def get_hero_by_id(
    hero_id: UUID,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a hero by its id
    """
    hero = await crud.hero.get(id=hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return create_response(data=hero)


@router.post("/powers", response_model=IPostResponseBase[IHeroReadWithPowersAndTeam])
async def create_hero(
    hero: IHeroCreateWithPowersAndTeams,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new hero
    """
    heroe = await crud.hero.create(obj_in=hero, created_by_id=current_user.id)
    return create_response(data=heroe)


@router.post("", response_model=IPostResponseBase[IHeroRead])
async def create_hero(
    hero: IHeroCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new hero
    """
    heroe = await crud.hero.create(obj_in=hero, created_by_id=current_user.id)
    return create_response(data=heroe)


@router.put("/{hero_id}", response_model=IPutResponseBase[IHeroRead])
async def update_hero(
    hero_id: UUID,
    hero: IHeroUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a hero by its id
    """
    current_hero = await crud.hero.get(id=hero_id)
    if not current_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    heroe_updated = await crud.hero.update(obj_new=hero, obj_current=current_hero)
    return create_response(data=heroe_updated)


@router.delete("/{hero_id}", response_model=IDeleteResponseBase[IHeroRead])
async def remove_hero(
    hero_id: UUID,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Deletes a hero by its id
    """
    current_hero = await crud.hero.get(id=hero_id)
    if not current_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    heroe = await crud.hero.remove(id=hero_id)
    return create_response(data=heroe)
