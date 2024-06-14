from DataManager import DataManager

class CitiesManager(DataManager):
    def __init__(self):
        super().__init__()
        self.register_entity_type("city")

    def get_city(self, city_id: str) -> object:
        return self.get("city", city_id)

    def save_city(self, city: object) -> bool:
        return self.save(city)

    def update_city(self, city: object) -> bool:
        return self.update(city)

    def delete_city(self, city_id: str) -> bool:
        return self.delete(city_id)