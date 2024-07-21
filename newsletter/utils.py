from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Subscription
from core.models import SiteSettings


def send_welcome_email(user):
    site_settings = SiteSettings.objects.first()
    site_name = SiteSettings.objects.first().site_name
    subject = f'Welcome to {site_name}!'
    html_message = render_to_string('newsletter/welcome_email.html', {'user': user, 'site_settings': site_settings,})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)


def send_new_post_email(post, recipients):
    subject = f'New Post: {post.title}'
    site_url = SiteSettings.objects.first().og_url
    site_settings = SiteSettings.objects.first()
    post_url = f'{site_url}{post.slug}/'  # Correct URL format
    print(f"Generated post URL: {post_url}")  # Debugging line
    html_message = render_to_string('newsletter/new_post_email.html', {'post': post, 'post_url': post_url, 'site_settings': site_settings,})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, plain_message, from_email, recipients, html_message=html_message)
    