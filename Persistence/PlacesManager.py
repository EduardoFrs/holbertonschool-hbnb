from DataManager import DataManager

class PlacesManager(DataManager):
    # PlacesManager subclass

    def __init__(self):
        super().__init__()
        self.register_entity_type("place")

    def get_place(self, place_id: str) -> object:
        return self.get("place", place_id)

    def save_place(self, place: object) -> bool:
        return self.save(place)

    def update_place(self, place: object) -> bool:
        return self.update(place)

    def delete_place(self, place_id: str) -> bool:
        return self.delete("place", place_id)