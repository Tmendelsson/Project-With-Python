from core.services.product_service import ProductService
from django.http import JsonResponse

class ProductController:
    def __init__(self):
        self.product_service = ProductService()
    
    def list_product(self, request):
        products = self.product_service.get_all_products()
        return JsonResponse({'products:':list(products.values())})
    
    def create_product(self, request):
        data = request.POST
        user = request.user
        product = self.product_service.create_product(
            data['name'],data['description'],data['launch_date'],data['price'],data['image']
        )
        return JsonResponse({'product:': product.name})