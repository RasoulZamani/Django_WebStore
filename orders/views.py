from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from home.models import Product
from .forms import CartAddForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Order, OrderItem
class CartView(View):
    """ orders cart CBV"""
    def get(self,request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart':cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id = product_id)
        addcart_form = CartAddForm(request.POST)
        if addcart_form.is_valid():
            cart.add_product(product, addcart_form.cleaned_data['quantity'])
        return redirect('orders:cart')

class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id = product_id)
        cart.remove_product(product)
        return redirect('orders:cart')
    

class CartFinalCostView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id = order_id)
        return render(request, 'orders/final_cost.html', {'order':order})


class CartConfirmView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order    = order,
                product  = item['product_name'],
                price    = item['price'],
                quantity = item['quantity'],
            )
        cart.clear_cart()
        return redirect('orders:cart_final_cost', order.id)
    
