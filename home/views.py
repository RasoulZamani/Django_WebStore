from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
    """CBV for home"""
    def get(self, request):
        return render(request, 'home/home.html' )