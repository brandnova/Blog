# content/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('category/<slug:category_slug>/', views.content_list, name='content_list_by_category'),
    path('tag/<slug:tag_slug>/', views.content_list, name='content_list_by_tag'),
    path('category/<slug:category_slug>/tag/<slug:tag_slug>/', views.content_list, name='content_list_by_category_and_tag'),
    path('create/', views.content_create, name='content_create'),
    path('<slug:slug>/', views.content_detail, name='content_detail'),

    path('<slug:slug>/like/', views.like_content, name='like_content'),
    path('<slug:slug>/dislike/', views.dislike_content, name='dislike_content'),

    
]
