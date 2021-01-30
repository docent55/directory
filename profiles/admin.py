from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.utils.translation import gettext, gettext_lazy as _

class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'middle_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('ext.Info'), {'fields': ('phone_number', 'avatar', 'gender')}),
    )

admin.site.register(UserProfile, UserProfileAdmin)