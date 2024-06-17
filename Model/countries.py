from dataclasses import dataclass
from base_model import BaseModel

@dataclass
class Country(BaseModel):
    _name: str = None
    _country_code: str = None
