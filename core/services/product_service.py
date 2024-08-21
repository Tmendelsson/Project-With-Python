from core.repositories.product_repository import ProductRepository

class ProductService: 
    def __init__(self) :
        self.product_repository = ProductRepository()
    
    def get_all_products(self):
        return self.product_repository.get_all_products()
    
    def create_product(self, name, description, launch_date, price, user, image):
        return self.product_repository.create_product(name, description, launch_date, price, user, image)