from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from manager import MyUserManager

class MyUser(AbstractBaseUser):
    """ customized user class"""
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin  = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone' 
    REQUIRED_FIELDS = ['email']
    
    objects = MyUserManager()
    
    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
