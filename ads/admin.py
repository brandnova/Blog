from django.contrib import admin
from .models import AdPlacement, Ad

@admin.register(AdPlacement)
class AdPlacementAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('placement', 'active', 'start_date', 'end_date')
    list_filter = ('placement', 'active')
    search_fields = ('placement__name',)
