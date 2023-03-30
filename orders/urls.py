from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/confirm/', views.CartConfirmView.as_view(), name='cart_confirm'),
    path('cart/FinalCost/<int:order_id>', views.CartFinalCostView.as_view(), name='cart_final_cost'),
    
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
]
