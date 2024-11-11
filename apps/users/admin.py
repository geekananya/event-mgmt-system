from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_admin')


    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
