from django.contrib import admin
from django.urls import path
from core.controllers.user_controller import UserController
from core.controllers.product_controller import ProductController

user_controller = UserController()
product_controller = ProductController()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create/',user_controller.create_user, name = 'create_user'),
    path('users/',user_controller.list_users, name='list_users'),
    path('products/create/',product_controller.create_product, name='create_product'),
    path('products/',product_controller.list_product, name='list_users')  
]
