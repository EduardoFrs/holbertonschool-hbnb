#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass
from pytz import timezone # pip import pytz # for timestamp to local timezone

Base = dataclass(frozen=False)

@Base
class BaseModel:
    id: str = str(uuid4())

    timestamp = 1655080000000 # ms since epoch
    timestamp_seconds = timestamp / 1000
    created_at = datetime.fromtimestamp(timestamp_seconds, timezone('Europe/Paris'))
    created_at_formatted = created_at.strftime("%Y-%m-%d %H:%M:%S %Z")

    updated_at = datetime.fromtimestamp(timestamp_seconds, timezone('Europe/Paris'))
    updated_at_formatted = updated_at.strftime("%Y-%m-%d %H:%M:%S %Z")
    # avec strftime: formatter le datetime object en string