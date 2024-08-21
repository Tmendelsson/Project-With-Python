from core.models import Product

class ProductRepository:
    def get_all_products(self):
        return Product.objects.all()
    
    def get_product_by_id(self, product_id):
        return Product.objects.filter(id=product_id).first()
    
    def create_product(self, name, description, launch_date, price, user, image):
        product = Product(
            name=name,
            description=description,
            launch_date=launch_date,
            price=price,
            added_by=user,
            image=image
        )
        product.save()
        return product