from django.contrib import admin
from .models import Profile, account_data
# Register your models here.


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone']
    list_filter = ['city']


class UserData(admin.ModelAdmin):
    list_display = ['username', 'key', 'value']
    list_filter = ['username']


admin.site.register(Profile, AdminProfile)
admin.site.register(account_data, UserData)
