from core.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def create_user(self, name, email, password, profile):
        return self.user_repository.create_user(name, email, password, profile)

