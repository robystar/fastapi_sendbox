from app.models.user_model import User
from app.schemas.common_schema import (
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    create_response,
)
from fastapi_pagination import Page, Params
from app.schemas.istanza_schema import (
    IIstanzaCreate,
    IIstanzaCreateAll,
    IIstanzaRead,
    IIstanzaUpdate,
    IIstanzaReadWithRichiedenti
)
from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app import crud
from uuid import UUID
from app.schemas.soggetto_schema import IRichiedenteCreate, IRichiedenteReadAll
from app.schemas.role_schema import IRoleEnum
from app.models.istanza_model import IstanzaBase, Istanza

router = APIRouter()


@router.get("", response_model=IGetResponseBase[Page[IIstanzaReadWithRichiedenti]])
async def get_istanze(
    params: Params = Depends(),
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a paginated list of istanze
    """
    istanzas = await crud.istanza.get_multi_paginated(params=params)
    return create_response(data=istanzas)


@router.get("/{istanza_id}", response_model=IGetResponseBase[IIstanzaRead])
async def get_istanza_by_id(
    istanza_id: int,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a istanza by its id
    """
    istanza = await crud.istanza.get(id=istanza_id)
    return create_response(data=istanza)

@router.get("/completa/{istanza_id}", response_model=IGetResponseBase[IIstanzaReadWithRichiedenti])
async def get_istanza_by_id(
    istanza_id: int,
    current_user: User = Depends(deps.get_current_user()),
):
    """
    Gets a istanza con richiedenti by its id
    """
    istanza = await crud.istanza.get(id=istanza_id)
    return create_response(data=istanza)


@router.post("", response_model=IPostResponseBase[IIstanzaRead])
async def create_istanza(
    istanza: IIstanzaCreate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new istanza
    """
    new_istanza = await crud.istanza.create(obj_in=istanza, created_by_id=current_user.id)
    return create_response(data=new_istanza)

@router.post("/{istanza_id}", response_model=IPostResponseBase[IIstanzaCreateAll])
async def create_istanza_with_id(
    istanza_id: int,
    istanza: IIstanzaCreateAll,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Creates a new istanza with id
    """
    new_istanza = await crud.istanza.create_istanza_with_id(obj_in=istanza, created_by_id=current_user.id, istanza_id=istanza_id)
    return create_response(data=new_istanza)


@router.put("/{istanza_id}", response_model=IPutResponseBase[IIstanzaRead])
async def update_istanza(
    istanza_id: int,
    istanza: IIstanzaUpdate,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Updates a istanza by its id
    """
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    istanza_updated = await crud.istanza.update(obj_current=istanza_current, obj_new=istanza)
    return create_response(data=istanza_updated)


@router.post(
    "/{istanza_id}/richiedenti", response_model=IPostResponseBase[IIstanzaReadWithRichiedenti]
)
async def add_richiedenti_to_istanza(
    istanza_id: int,
    richiedente: IRichiedenteReadAll,
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Adds a richiedenti to istanza
    """
    
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    richiedente.istanza_id = istanza_id
    new_richiedente = await crud.richiedente.create(obj_in=richiedente)
    istanza = await crud.istanza.add_richiedente_to_istanza(richiedente=new_richiedente, istanza_id=istanza_id)
    return create_response(message="User added to istanza", data=istanza)



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