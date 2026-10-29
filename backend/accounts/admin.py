from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Rol y Contacto', {'fields': ('role', 'telefono')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información de Rol y Contacto', {'fields': ('role', 'telefono')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)