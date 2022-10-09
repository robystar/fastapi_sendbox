from typing import Dict, List, Union
from sqlmodel.ext.asyncio.session import AsyncSession
from app import crud
from app.schemas.role_schema import IRoleCreate
from app.core.config import settings
from app.schemas.user_schema import IUserCreate
from app.schemas.team_schema import ITeamCreate, ITeamCreateWithWeapons
from app.schemas.hero_schema import IHeroCreate, IHeroCreateWithPowersAndTeams
from app.schemas.group_schema import IGroupCreate
from app.schemas.power_schema import IPowerCreate
from app.schemas.weapon_schema import IWeaponCreate
from app.models.team_model import Team
from app.models.weapon_model import Weapon
from app.models.hero_model import Hero
from app.models.power_model import Power

from app.models.anagrafe_model import Anagrafe





async def prove(session:AsyncSession):
    anag = await crud.anagrafe.get_anagrafe_by_id(id=128, db_session=session)
    return anag


async def prova_db(session: AsyncSession) -> None:
    
        wep_1 = Weapon(name="Alabarda", description="Alabarda spaziale")
        wep_2 = Weapon(name="Razzo missile", description="Razzo missile")
        wep_3 = Weapon(name="Spada laser", description="Spada laser")

        pow_1 = Power(name="Fuoco", description="Potenza di fuoco")
        pow_2 = Power(name="Invisibile", description="Invisibile")
        pow_3 = Power(name="Postit", description="Postit")
        pow_4 = Power(name="Spaccabraccia", description="Spaccabraccia")
                    
        team_1 = Team(name="TEAM1", headquarters="Sharp Tower", weapons=[wep_1,wep_2,wep_3])
        team_2 = Team(name="TEAM2", headquarters="Sister Margaret’s Bar", weapons=[wep_1,wep_2,wep_3])


        import pdb;pdb.set_trace()
        
        team_3 = await crud.team.get_team_by_name(name="TEAM1", db_session=session)
        weap_4 = await crud.weapon.get_weapon_by_name(name="Alabarda", db_session=session)
        pow_5 = await crud.power.get_power_by_name(name="Fuoco", db_session=session)
        
        hero = IHeroCreateWithPowersAndTeams(name="aaaaaaaaa", secret_name="aaaaaaaaaaaaa", age=21, teams=[Team.from_orm(team_3)], powers=[Power.from_orm(pow_5)])

        xx = Team.from_orm(team_3)
        await crud.hero.create(created_by_id="a6ef8813-e47b-4da4-93fc-6aa1893b494f", obj_in=hero, db_session=session)

















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

weapons: List[IWeaponCreate] = [
    IWeaponCreate(name="Alabarda", description="Alabarda spaziale"),
    IWeaponCreate(name="Razzo missile", description="Razzo missile"),
    IWeaponCreate(name="Spada laser", description="Spada laser"),
]

teams: List[Dict[str, Union[List[str], Team]]] = [
    {
        "data": Team(name="Preventers", headquarters="Sharp Tower"),
    
        "weapons": ["Alabarda","Spada laser"]
    },
    {
        "data": Team(name="Z-Force", headquarters=f"Sister Margaret's Bar"),
        "weapons": ["Razzo missile","Spada laser"]
    },    
    {
        "data": Team(name="Team smart", headquarters="Casa Mia"),
        "weapons": ["Alabarda","Spada laser","Razzo missile"]
    },    
    {
        "data": Team(name="A-Team", headquarters=f"Casa d'altri"),
        "weapons": ["Alabarda"]
    },   
]
    

powers: List[IPowerCreate] = [
    IPowerCreate(name="Fuoco", description="Potenza di fuoco"),
    IPowerCreate(name="Invisibile", description="Invisibile"),
    IPowerCreate(name="Postit", description="Postit"),
    IPowerCreate(name="Spaccabraccia", description="Spaccabraccia")
]



heroes: List[Dict[str, Union[List[str], IHeroCreateWithPowersAndTeams]]] = [
    {
        "data": IHeroCreateWithPowersAndTeams(name="Deadpond", secret_name="Dive Wilson", age=21, teams=[], powers=[]),
        "teams": ["Z-Force","Peventers"],
        "powers": ["Fuoco","Postit"]
    },
    {
        "data": IHeroCreateWithPowersAndTeams(name="Rusty-Man", secret_name="Tommy Sharp", age=48, teams=[], powers=[]),
        "teams": ["Preventers","A-Team"],
        "powers": ["Invisibile"]
    },
    {
        "data": IHeroCreateWithPowersAndTeams(name="Chitarrista", secret_name="Chitarrista", age=48, teams=[], powers=[]),
        "teams": ["Team smart","A-Team"],
        "powers": ["Spaccabraccia"]
    } 
]







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

    for weapon in weapons:
        current_weapon = await crud.weapon.get_weapon_by_name(name=weapon.name, db_session=db_session)
        if not current_weapon:
            await crud.weapon.create(obj_in=weapon, db_session=db_session)  
     
    import pdb;pdb.set_trace()

    for x in teams:
        current_team = await crud.team.get_team_by_name(name=x["data"].name, db_session=db_session)
        if not current_team:
            '''
            weaps:List[Weapon]=[]
            for x in obj["weapons"]:
                weapon = await crud.weapon.get_weapon_by_name(name=x, db_session=db_session)
                if weapon:
                    weaps.append(weapon)
            new_team:Team = obj["data"]
            new_team.weapons =weaps
            '''   
            new_team:Team = x["data"]
            await crud.team.create(obj_in=new_team, db_session=db_session)
      
    import pdb;pdb.set_trace()

    for power in powers:
        current_power = await crud.power.get_power_by_name(name=power.name, db_session=db_session)
        if not current_power:
            await crud.power.create(obj_in=power, db_session=db_session)       

    for obj in heroes:
        current_heroe = await crud.hero.get_heroe_by_name(name=obj["data"].name, db_session=db_session)
        if not current_heroe:
            tms:List[Team]=[]
            for x in obj["teams"]:
                team = await crud.team.get_team_by_name(name=x, db_session=db_session)
                if team:
                    tms.append(team)

            
            new_heroe = obj["data"]
            new_heroe.teams = tms
            await crud.hero.create(obj_in=new_heroe, db_session=db_session)
    