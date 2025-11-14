from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  
from django.contrib.admin.sites import AdminSite

class MyAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser

admin_site = MyAdminSite(name='myadmin')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
