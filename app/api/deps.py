from typing import AsyncGenerator, List
from uuid import UUID
from fastapi import Depends, HTTPException, status
from app.schemas.user_schema import IUserCreate
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.models.user_model import User
from pydantic import ValidationError
from app import crud
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
from sqlmodel.ext.asyncio.session import AsyncSession
from app.schemas.common_schema import IMetaGeneral

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

async def get_general_meta() -> IMetaGeneral:
    current_roles = await crud.role.get_multi(skip=0, limit=100)
    return IMetaGeneral(roles=current_roles)

def get_current_user(required_roles: List[str] = None) -> User:
    async def current_user(token: str = Depends(reusable_oauth2)) -> User:        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
        except (jwt.JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
        user: User = await crud.user.get(id=payload["sub"])
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")

        if required_roles:
            is_valid_role = False
            for role in required_roles:
                if role == user.role.name:
                    is_valid_role = True
                    
            if is_valid_role == False:
                raise HTTPException(
                    status_code=403,
                    detail=f'Role "{required_roles}" is required to perform this action',
                )
        
        
        return user

    return current_user


async def user_exists(new_user: IUserCreate) -> IUserCreate:
    user = await crud.user.get_by_email(email=new_user.email)
    if user:
        raise HTTPException(
            status_code=404, detail="There is already a user with same email"
        )
    return new_user

async def is_valid_user(user_id: UUID) -> UUID:
    user = await crud.user.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User no found")
        
    return user_id

