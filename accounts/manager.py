from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    """customized manager"""
    
    def create_user(self, phone, email, password):
        
        if not phone:
            raise ValueError("user must have phone number")
        
        if not email:
            raise ValueError("user must have email address")
        
        user = self.model(phone=phone, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, email, password):
        user = self.create_user( phone, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    
        
        
        
        
        
        
        
        
        
        
        