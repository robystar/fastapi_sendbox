from typing import Optional
from unicodedata import numeric
import uuid as uuid_pkg
from sqlmodel import SQLModel as _SQLModel, Field
from sqlalchemy.orm import declared_attr
from datetime import datetime

class SQLModel(_SQLModel):
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__

class BaseUUIDModel(SQLModel):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    updated_at: Optional[datetime]
    created_at: Optional[datetime]

class BaseJoinUUIDModel(SQLModel):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    
