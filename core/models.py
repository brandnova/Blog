from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField # type: ignore

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    site_description = models.TextField()
    favicon = models.ImageField(upload_to='Site_images/', null=True, blank=True)
    logo = models.ImageField(upload_to='Site_images/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    # Meta Tags Fields
    meta_keywords = models.CharField(max_length=255, help_text="Comma-separated SEO keywords for the site")
    meta_description = models.CharField(max_length=255, help_text="Meta description for the site")
    meta_author = models.CharField(max_length=100, help_text="Author of the site content")
    
    # Open Graph Tags
    og_title = models.CharField(max_length=255, help_text="Open Graph title for the site")
    og_description = models.CharField(max_length=255, help_text="Open Graph description for the site")
    og_image = models.ImageField(upload_to='meta_images/', blank=True, null=True, help_text="Open Graph image for the site")
    og_url = models.URLField(help_text="Open Graph URL for the site")
    
    def __str__(self):
        return self.site_name

class StaticPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title