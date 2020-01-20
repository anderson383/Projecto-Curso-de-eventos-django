from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups','user_permissions')
    list_filter = ('is_superuser',)
    fieldsets = (
        ('User',{'fields':('username','password')}),
        ('Información Personal',{'fields':
            ('first_name','last_name', 'email', 'avatar')}),
        ('Permisos',{'fields':(
            'is_active',
            'is_superuser',
            'groups',
            'user_permissions'
            )}),
    )