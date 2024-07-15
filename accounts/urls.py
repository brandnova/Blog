from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Password reset views
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), 
         name='reset_password'),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
         name='password_reset_complete'),
    
    # Password change view
    path('password_change/', views.password_change, name='password_change'),
]
