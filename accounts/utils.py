from django.utils import timezone
from datetime import timedelta
from .models import Badge, Profile
from content.models import Content, Comment

def assign_badges(user):
    profile = Profile.objects.get(user=user)

    # Veteran User
    if user.date_joined < timezone.now() - timedelta(days=365):
        badge, created = Badge.objects.get_or_create(name='Veteran User')
        profile.badges.add(badge)

    # New User
    if user.date_joined >= timezone.now() - timedelta(days=30):
        badge, created = Badge.objects.get_or_create(name='New User')
        profile.badges.add(badge)

    # Content Creator
    if Content.objects.filter(author=user).count() >= 10:
        badge, created = Badge.objects.get_or_create(name='Content Creator')
        profile.badges.add(badge)

    # Top Commenter
    if Comment.objects.filter(author=user).count() >= 50:
        badge, created = Badge.objects.get_or_create(name='Top Commenter')
        profile.badges.add(badge)

    # Popular Author
    user_likes_count = sum(content.likes.count() for content in Content.objects.filter(author=user))
    if user_likes_count >= 100:
        badge, created = Badge.objects.get_or_create(name='Popular Author')
        profile.badges.add(badge)

    # Active User
    if (timezone.now() - user.last_login) < timedelta(days=7):
        badge, created = Badge.objects.get_or_create(name='Active User')
        profile.badges.add(badge)

    # Reviewer
    if Comment.objects.filter(author=user).values('content').distinct().count() >= 20:
        badge, created = Badge.objects.get_or_create(name='Reviewer')
        profile.badges.add(badge)

    # Admin
    if user.is_superuser:
        badge, created = Badge.objects.get_or_create(name='Admin')
        profile.badges.add(badge)

    # Author
    if user.groups.filter(name='Author').exists():
        badge, created = Badge.objects.get_or_create(name='Author')
        profile.badges.add(badge)

    # Save the profile after adding badges
    profile.save()
