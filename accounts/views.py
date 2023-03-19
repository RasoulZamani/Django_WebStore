from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm, VerifyRegisterCode
from .models import OtpCode, MyUser
from utils import send_otp_code
import random

class UserRegisterView(View):
    """cbv for registering users"""
    class_form = UserRegisterForm
    template_adrs= 'accounts/register.html'
    
    def get(self, request):
        return render(request, self.template_adrs, {'register_form':self.class_form})
    
    def post(self, request):
        register_form = self.class_form(request.POST)
        if register_form.is_valid():
            rand_code = random.randint(1000,9999)
            phone = register_form.cleaned_data['phone']
            send_otp_code(phone, rand_code)
            OtpCode.objects.create(phone=phone, code=rand_code)            
            request.session['user_reg_inf'] = {
                'phone':phone,
                'email':register_form.cleaned_data['email'],
                'password':register_form.cleaned_data['password']
            }
            messages.success(request, 'verification code was sent to {phone}','success')
            return redirect('accounts:user_verify_code')
        
        return render(request, self.template_adrs,{'register_form':register_form})
    
    
class UserRegisterVerifyCode(View):
    """verifying code"""
    class_form =  VerifyRegisterCode 
    def get(self, request):
        return render(request, 'accounts/verify.html', {'verify_form':self.class_form})
    
    def post(self, request):
        verify_form = self.class_form(request.POST)
        user_session = request.session['user_reg_inf']
        code_ins = OtpCode.objects.get(phone=user_session['phone'])
        if verify_form.is_valid():
            cd = verify_form.cleaned_data
            if cd['code'] == code_ins.code:
                MyUser.objects.create_user(email=user_session['email'],
                                           phone=user_session['phone'],
                                           password=user_session['password']
                )
                code_ins.delete()
                messages.success(request,"code is verified seccessffuly", 'success')
                return redirect('home:home')
            else:
                messages.error(request, "wrong code!",'danger')
                return redirect('accounts:user_verify_code')
                
        return redirect('home:home')
    
    
