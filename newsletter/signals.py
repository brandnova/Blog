from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from newsletter.utils import send_welcome_email
from .models import Subscription
from django.contrib.auth.models import User
from content.models import Content  # Adjust the import according to your project structure
from core.models import SiteSettings

@receiver(post_save, sender=User)
def send_welcome_email_signal(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance)


@receiver(post_save, sender=Content)
def send_new_post_email(sender, instance, created, **kwargs):
    if created:
        post = instance
        recipients = Subscription.objects.values_list('email', flat=True)
        subject = f'New Post: {post.title}'
        site_url = SiteSettings.objects.first().og_url  # Fetch the site URL from SiteSettings
        post_url = f'{site_url}{post.get_absolute_url()}'  # Correctly concatenate URL
        html_message = render_to_string('newsletter/new_post_email.html', {'post': post, 'post_url': post_url})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        
        send_mail(subject, plain_message, from_email, recipients, html_message=html_message)
