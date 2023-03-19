from django import forms
from .models import MyUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    pass1 = forms.CharField(label='password',widget=forms.PasswordInput)
    pass1 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
 
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
        user.set_password(self.cleaned_dada['pass1'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text = 'you can chang your password from<a href="../password/"> this form </a>')
    class Meta:
        model = MyUser
        fields = ('email', 'phone', 'password', 'last_login')
            