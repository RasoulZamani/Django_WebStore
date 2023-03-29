""" we separate cart session handling in this file"""
from home.models import Product
class Cart:
    def __init__(self, request):
       self.session = request.session
       cart = self.session.get('cart')
       if not cart:
           # when user adds product to cart for first time we need create session:
           cart = self.session['cart'] = {}    
       self.cart = cart
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product_name'] = product
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item
       
       
    def add_product(self,product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':product.price}
        self.cart[product_id]['quantity'] += quantity
        self.session.modified = True


    def remove_product(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        
        
    def get_total_price(self):
    
        return sum(item['quantity']* int(item['price']) for item in self.cart.values())