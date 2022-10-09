from typing import Dict, List, Union
from sqlmodel.ext.asyncio.session import AsyncSession

import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))



from app.db.session import SessionLocal

from app import crud
from app.schemas.role_schema import IRoleCreate
from app.core.config import settings
from app.schemas.user_schema import IUserCreate
from app.schemas.team_schema import ITeamCreate
from app.schemas.hero_schema import IHeroCreate
from app.schemas.group_schema import IGroupCreate


from app.models.team_model import Team



roles: List[IRoleCreate] = [
    IRoleCreate(name="admin", description="This the Admin role"),
    IRoleCreate(name="manager", description="Manager role"),
    IRoleCreate(name="user", description="User role"),
]

groups: List[IGroupCreate] = [
    IGroupCreate(name="GR1", description="This is the first group")
]

users: List[Dict[str, Union[str, IUserCreate]]] = [
    {
        "data": IUserCreate(
            first_name="Admin",
            last_name="FastAPI",
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email=settings.FIRST_SUPERUSER_EMAIL,
            is_superuser=True,
        ),
        "role": "admin",
    },
    {
        "data": IUserCreate(
            first_name="Manager",
            last_name="FastAPI",
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email="manager@example.com",
            is_superuser=False,
        ),
        "role": "manager",
    },
    {
        "data": IUserCreate(
            first_name="User",
            last_name="FastAPI",
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email="user@example.com",
            is_superuser=False,
        ),
        "role": "user",
    },
]

teams: List[ITeamCreate] = [
    ITeamCreate(name="Preventers", headquarters="Sharp Tower"),
    ITeamCreate(name="Z-Force", headquarters=f"Sister Margaret's Bar"),
]

heroes: List[Dict[str, Union[str, IHeroCreate]]] = [
    {
        "data": IHeroCreate(name="Deadpond", secret_name="Dive Wilson", age=21),
        "team": "Z-Force",
        "is_training": True
    },
    {
        "data": IHeroCreate(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
        "team": "Preventers",
        "is_training": False
    },
]


async def create_heroes()->None:
    
    import pdb;pdb.set_trace()
    
    import uuid
    from app.models.hero_model import Hero

    async with SessionLocal() as session:

        
        team_1 = Team(name="TEAM1", headquarters="Sharp Tower")
        team_2 = Team(name="TEAM2", headquarters="Sister Margaret’s Bar")

        hero_1 = Hero(
            name="Eroe1",
            secret_name="Dive Wilson",
            teams=[team_1, team_2],
        )
        hero_2 = Hero(
            name="Eroe2",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_1],
        )
        hero_3 = Hero(
            name="Eroe3", secret_name="Pedro Parqueador", teams=[team_2]
        )
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        await session.commit()

        #await session.refresh(hero_1)
        #await session.refresh(hero_2)
        #await session.refresh(hero_3)
        
        

    



async def init_db(db_session: AsyncSession) -> None:

    for role in roles:
        role_current = await crud.role.get_role_by_name(
            name=role.name, db_session=db_session
        )
        if not role_current:
            await crud.role.create(obj_in=role, db_session=db_session)

    for user in users:
        current_user = await crud.user.get_by_email(
            email=user["data"].email, db_session=db_session
        )
        role = await crud.role.get_role_by_name(
            name=user["role"], db_session=db_session
        )
        if not current_user:
            user["data"].role_id = role.id
            await crud.user.create_with_role(obj_in=user["data"], db_session=db_session)

    for group in groups:
        current_group = await crud.group.get_group_by_name(name=group.name, db_session=db_session)
        if not current_group:
            new_group = await crud.group.create(obj_in=group, db_session=db_session)
            current_users = []
            for user in users:
                current_users.append(
                    await crud.user.get_by_email(email=user["data"].email, db_session=db_session)
                )
            await crud.group.add_users_to_group(
                users=current_users, group_id=new_group.id, db_session=db_session
            )

    for team in teams:
        current_team = await crud.team.get_team_by_name(name=team.name, db_session=db_session)
        if not current_team:
            await crud.team.create(obj_in=team, db_session=db_session)

    for heroe in heroes:
        current_heroe = await crud.hero.get_heroe_by_name(name=heroe["data"].name, db_session=db_session)
        team = await crud.team.get_team_by_name(name=heroe["team"], db_session=db_session)
        if not current_heroe:
            new_heroe = heroe["data"]
            #new_heroe.team_id = team.id
            await crud.hero.create(obj_in=new_heroe, db_session=db_session)
