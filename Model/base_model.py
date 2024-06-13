#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass
from pytz import timezone # pip import pytz # for timestamp to local timezone

Base = dataclass(frozen=True)

@Base
class BaseModel:
    id: str = str(uuid4())

    # created_at: datetime = datetime.now(timezone)
    # updated_at: datetime = datetime.now(timezone)

    timestamp = 1655080000000 # ms since epoch
    timestamp_seconds = timestamp / 1000
    created_at = datetime.fromtimestamp(timestamp_seconds, timezone('Europe/Paris'))
    created_at_formatted = created_at.strftime("%Y-%m-%d %H:%M:%S %Z")

    print(created_at_formatted)

    updated_at = datetime.fromtimestamp(timestamp_seconds, timezone('Europe/Paris'))
    updated_at_formatted = updated_at.strftime("%Y-%m-%d %H:%M:%S %Z")
    # avec strftime: formatter le datetime object en string

    print(updated_at_formatted)