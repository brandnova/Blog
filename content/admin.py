from django.contrib import admin
from django.db import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget # type: ignore
from .models import Content, Category, Genre, Tag

admin.site.register(Genre)

# Admin class for Content model
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }

# Admin class for Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Assuming Category has 'name' and 'slug' fields
    prepopulated_fields = {'slug': ('name',)}

# Admin class for Tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Assuming Tag has 'name' and 'slug' fields
    prepopulated_fields = {'slug': ('name',)}
