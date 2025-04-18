from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class AccoutsUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, UserAdmin)
