from dataclasses import dataclass
from base_model import BaseModel
from countries import Country

@dataclass
class City(BaseModel):
    name: str = None
    country: Country = None

