from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category

class HomeView(View):
    """CBV for home"""
    def get(self, request,category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()
        if category_slug:
           category = Category.objects.get(slug=category_slug)
           products = products.filter(category=category) 
        return render(request, 'home/home.html', {'products':products, 'categories': categories})
    
class ProductDetailView(View):
    def get(self,request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/details.html', {'product':product})