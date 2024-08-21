from core.models import User

class UserRepository:
    def get_all_users(self):
        return User.objects.all()
    
    def get_user_by_email(self, email):
        return User.objects.filter(email=email).first()
    
    def create_user(self, name, email, password, profile):
        user = User(name=name, email=email,profile=profile)
        user.set_password(password)
        user.save()
        return user