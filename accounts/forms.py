from django import forms
from .models import MyUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    pass1 = forms.CharField(label='password',widget=forms.PasswordInput)
    pass2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
 
    class Meta:
        model = MyUser
        fields = ('email', 'phone')
        
    def clean_pass2(self):
        cd = self.cleaned_data
        if cd['pass1'] and cd['pass2'] and cd['pass1']!= cd['pass2'] :
            raise ValidationError('password should be equal')
        return cd['pass2']
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['pass1'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text = 'you can chang your password from<a href="../password/"> this form </a>')
    class Meta:
        model = MyUser
        fields = ('email', 'phone', 'password', 'last_login')


class UserRegisterForm(forms.Form):
    email    = forms.EmailField(max_length=255)
    phone    = forms.CharField(max_length=11)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

    def clean_email(self):
        """checking uniqeness of email"""
        email = self.cleaned_data['email']
        user = MyUser.objects.filter(email=email).exists()
        if user:
            raise ValidationError("This email is already exists")
        return email
    
    def clean_phone(self):
        """checking uniqeness of phone"""
        phone = self.cleaned_data['phone']
        user = MyUser.objects.filter(phone=phone).exists()
        if user:
            raise ValidationError("This phone is already exists")
        return phone
        
        
class VerifyRegisterCode(forms.Form):
    """user enter recieved code here for verification"""
    code = forms.IntegerField()
    