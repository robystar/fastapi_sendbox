from typing import List
from app.models.ubicazione_model import UbicazioneBase
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
    IIstanzaReadWithTecnici,
    IIstanzaReadWithUbicazione,
    IIstanzaUpdate,
    IIstanzaReadWithRichiedenti,
    IIstanzaUpdateAll
)
from fastapi import APIRouter, Depends, HTTPException, Body
from app.api import deps
from app import crud
from uuid import UUID
from app.schemas.soggetto_schema import IRichiedenteCreate, IRichiedenteCreateAll, IRichiedenteReadAll, ITecnicoCreate, ITecnicoRead
from app.schemas.role_schema import IRoleEnum
from app.models.istanza_model import IstanzaBase, Istanza
from app.schemas.ubicazione_schema import ICivicoCreate, IPosizioneCreate, IUbicazioneCreate, IMappale_nceuCreate, IMappale_nctCreate

from .examples import istanza, istanza_con_richiedenti, richiedente, richiedenti, tecnico, tecnici, istanza_con_richiedenti, ubicazione

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
    istanza: IIstanzaCreate = Body(
        example=istanza,
    ),
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
    istanza: IIstanzaCreateAll = Body(
        example=istanza_con_richiedenti,
    ),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Crea istanza completa doca id con richiedenti (dump plomino doc)
    """
    new_istanza = await crud.istanza.create_istanza_with_id(obj_in=istanza, created_by_id=current_user.id, istanza_id=istanza_id)
    return create_response(data=new_istanza)

@router.put("/{istanza_id}", response_model=IPostResponseBase[IIstanzaUpdateAll])
async def update_istanza_with_id(
    istanza_id: int,
    istanza: IIstanzaUpdateAll = Body(
        example=istanza_con_richiedenti,
    ),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Aggiorna istanza completa doc id con richiedenti (dump plomino doc)
    """
    
    import pdb;pdb.set_trace()
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    istanza_updated = await crud.istanza.update(obj_current=istanza_current, obj_new=istanza_current)
    
    
    #istanza = await crud.istanza.update_istanza_with_id(obj_in=istanza, istanza_id=istanza_id)
    
    return create_response(data=istanza_updated)



@router.patch("/{istanza_id}", response_model=IPutResponseBase[IIstanzaRead])
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


@router.put(
    "/{istanza_id}/richiedenti", response_model=IPostResponseBase[IIstanzaReadWithRichiedenti]
)
async def update_richiedenti_istanza(
    istanza_id: int,
    richiedenti: List[IRichiedenteCreateAll] = Body(example=richiedenti),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Update richiedenti di istanza
    """
    
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    istanza = await crud.istanza.update_richiedenti_istanza(richiedenti=richiedenti, istanza_id=istanza_id)
    return create_response(message="User added to istanza", data=istanza)


@router.post(
    "/{istanza_id}/richiedente", response_model=IPostResponseBase[IIstanzaReadWithRichiedenti]
)
async def add_richiedente_to_istanza(
    istanza_id: int,
    richiedente: IRichiedenteReadAll = Body(example=richiedente),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Adds a richiedente to istanza
    """
    
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    richiedente.istanza_id = istanza_id
    new_richiedente = await crud.richiedente.create(obj_in=richiedente)
    istanza = await crud.istanza.add_richiedente_to_istanza(richiedente=new_richiedente, istanza_id=istanza_id)
    return create_response(message="User added to istanza", data=istanza)


@router.put(
    "/{istanza_id}/tecnici", response_model=IPostResponseBase[IIstanzaReadWithTecnici]
)
async def update_tecnici_istanza(
    istanza_id: int,
    tecnici: List[ITecnicoCreate] = Body(example=tecnici),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Update tecnici di istanza
    """
    
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    istanza = await crud.istanza.update_tecnici_istanza(tecnici=tecnici, istanza_id=istanza_id)
    return create_response(message="User added to istanza", data=istanza)


@router.post(
    "/{istanza_id}/tecnico", response_model=IPostResponseBase[IIstanzaReadWithTecnici]
)
async def add_tecnico_to_istanza(
    istanza_id: int,
    tecnico: ITecnicoRead = Body(example=tecnico),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Adds a tecnico to istanza
    """
    
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    tecnico.istanza_id = istanza_id
    new_tecnico = await crud.tecnico.create(obj_in=tecnico)
    istanza = await crud.istanza.add_tecnico_to_istanza(tecnico=new_tecnico, istanza_id=istanza_id)
    return create_response(message="User added to istanza", data=istanza)


@router.put(
    "/{istanza_id}/ubicazione", response_model=IPostResponseBase[IIstanzaReadWithUbicazione]
)
async def update_ubicazione_istanza(
    istanza_id: int,
    ubicazione: IUbicazioneCreate = Body(example = ubicazione),
    current_user: User = Depends(
        deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
    ),
):
    """
    Update ubicazione di istanza
    """
    
    istanza_current = await crud.istanza.get(id=istanza_id)
    if not istanza_current:
        raise HTTPException(status_code=404, detail="Istanza not found")

    istanza = await crud.istanza.update_ubicazione_istanza(ubicazione=ubicazione, istanza_id=istanza_id)
    return create_response(message="User added to istanza", data=istanza)

