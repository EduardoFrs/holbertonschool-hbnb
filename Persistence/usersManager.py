from Persistence.repository import DataManager
from ..Model.user import User

class UserManager(DataManager):
    # Manages users data persistence
    # inherits from DataManager class and assumes user's entities have ID and attr
    # -> inclus le _save_data du coup toutes les actions sont updatées sur le JSON
    def __init__(self):
        super().__init__()
        self.register_entity_type("user")

    def get_user(self, user_id: str) -> object:
        # Retrieves a user based on ID
        # Args: user_id
        # Returns: user object if found or None
        return self.get("user", user_id)

    def save_user(self, user: object) -> bool:
        # Saves a user obj to data store
        self._save_data(user)
        return self.save(user)

    def update_user(self, user: object) -> bool:
        return self.update(user)

    def delete_user(self, user_id: str) -> bool:
        return self.delete("user", user_id)