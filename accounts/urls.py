from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('verifycode/', views.UserRegisterVerifyCode.as_view(), name='user_verify_code'),
]


