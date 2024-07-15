# core/admin.py

from django.contrib import admin
from .models import SiteSettings, StaticPage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'phone_number', 'meta_keywords', 'meta_description', 'meta_author')
    fieldsets = (
        (None, {
            'fields': ('site_name', 'site_description', 'favicon', 'logo', 'address', 'contact_email', 'phone_number')
        }),
        ('Meta Tags', {
            'fields': ('meta_keywords', 'meta_description', 'meta_author')
        }),
        ('Open Graph Tags', {
            'fields': ('og_title', 'og_description', 'og_image', 'og_url')
        }),
    )

@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
