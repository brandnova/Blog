from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from content.models import Content, Comment
from accounts.utils import assign_badges
from .models import Content


@receiver(post_save, sender=Content)
def content_post_save(sender, instance, created, **kwargs):
    if created:
        assign_badges(instance.author)

@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, created, **kwargs):
    if created:
        assign_badges(instance.author)

