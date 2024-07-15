from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'user__email')

# You can customize further admin configurations as needed
