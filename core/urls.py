from django.urls import path
from .views import *
from content import views

urlpatterns = [
    path('', index, name='index'),
    path('pages/<slug:slug>/', static_page_view, name='static_page'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('content/<slug:slug>/', views.content_detail, name='content_detail'),
    path('search/', views.search_results, name='search_results'),
]
