from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Subscription
from .forms import SubscriptionForm
from content.models import Content
from core.models import SiteSettings
from accounts.models import Profile
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to the newsletter.')
            return redirect('index')  # Redirect to a success page or the home page
    else:
        form = SubscriptionForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


def email_temp(request, slug, user_id):
    post = get_object_or_404(Content, slug=slug)
    user = get_object_or_404(Profile.user, id=user_id)
    site_settings = SiteSettings.objects.first()
    site_url = site_settings.og_url
    post_url = f'{site_url}{post.get_absolute_url()}'
    
    context = {
        'user': user,
        'post': post,
        'post_url': post_url,
        'site_settings': site_settings,
    }
    
    return render(request, 'newsletter/email_base.html', context)

# def welcome_email(request, user_id):
#     user = get_object_or_404(Profile.user, id=user_id)
#     site_settings = SiteSettings.objects.first()
    
#     context = {
#         'user': user,
#         'site_settings': site_settings,
#     }
    
#     return render(request, 'newsletter/welcome_email.html', context)