from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from home.models import Product
from .forms import CartAddForm


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