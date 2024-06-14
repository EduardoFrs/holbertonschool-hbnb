from DataManager import DataManager

class CountriesManager(DataManager):
    def __init__(self):
        super().__init__()
        self.register_entity_type("country")

    def get_country(self, country_id: str) -> object:
        return self.get("country", country_id)

    def save_country(self, country: object) -> bool:
        return self.save(country)

    def update_country(self, country: object) -> bool:
        return self.update(country)

    def delete_country(self, country_id: str) -> bool:
        return self.delete("country", country_id)