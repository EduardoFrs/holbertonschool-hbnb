from dataclasses import dataclass
from base_model import BaseModel

@dataclass
class Country(BaseModel):
    _name: str = None
    _country_code: str = None


    """
    No need for upcoming code
    -> direct access self.country_code without property def

    @property
    def country_code(self):
        return self.__country_code

    To access -> country_object.country_code
    """