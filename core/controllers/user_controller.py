from core.services.user_service import UserService
from django.http import JsonResponse

class UserController: 
    def __init__(self):
        self.user_Service = UserService()
    
    def list_users(self, request):
        users = self.user_Service.get_all_users()
        return JsonResponse({"users":list(users.values())})
    
    def create_user(self, request):
        data = request.POST
        user = self.user_Service.create_user(data['name'],data['email'],data['password'],data['profile'])
        return JsonResponse({"user:":user.email})