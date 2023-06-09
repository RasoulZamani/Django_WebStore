from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import MyUser, OtpCode

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email','phone', 'is_active')
    list_filter  = ('is_admin',)
    fieldsets = (
        ('main info', {"fields": ('email','phone','password')}),
        ('permission', {"fields": ('is_active','is_admin', 'last_login','groups','user_permissions')})
    )
    add_fieldsets = (
        (None, {'fields':('email','phone','pass1','pass2')}),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups','user_permissions')
    
admin.site.unregister(Group)
admin.site.register(MyUser, MyUserAdmin)

    
@admin.register(OtpCode)
class OptCodeAdmin(admin.ModelAdmin):
    list_display = ('phone','code', 'created')
