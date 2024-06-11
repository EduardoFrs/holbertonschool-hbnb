#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime, timezone
from dataclasses import dataclass

Base = dataclass(frozen=True)

@Base
class BaseModel:
    """
    Base class for all models
    """
    id: str = str(uuid4())
    """
    datetime.utc() is deprecated, have to use timezone.utc
    """
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)
