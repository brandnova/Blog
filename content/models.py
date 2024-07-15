from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField # type: ignore

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='content-imgs', blank=True, default='default.jpg')
    highlight = models.TextField(help_text="Do not start the highlight with a symbol or punctuation (Always a text)")
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='Genres', blank=True)
    tags = models.ManyToManyField(Tag, related_name='Contents', blank=True)

    likes = models.ManyToManyField(User, related_name='Content_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='Content_dislikes', blank=True)

    def __str__(self):
        return self.title
