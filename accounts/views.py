from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from ads.models import Ad
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CustomAuthenticationForm, CustomPasswordChangeForm
from django.contrib import messages
from content.models import Content, Comment
from django.utils import timezone
from datetime import timedelta
# from newsletter.models import Subscription


def register(request):
    # Redirect authenticated users to the profile page
    if request.user.is_authenticated:
        return redirect('profile')
    
    # Process form submission
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # send_registration_email(user)
            login(request, user)  # Log the user in after registration
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('profile')  # Redirect to profile page after successful registration
    else:
        form = UserRegisterForm()
    
    # Render registration form for GET request
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


@login_required
def profile(request):
    user_contents_count = Content.objects.filter(author=request.user).count()
    user_comments_count = Comment.objects.filter(author=request.user).count()
    ads_base = Ad.objects.filter(placement__name="Base", active=True).first()

    # if user_contents_count >= 10:
        # send_badge_email(request.user, 'Content Creator')

    user_likes_count = sum(content.likes.count() for content in Content.objects.filter(author=request.user))
    user_registration_duration = timezone.now() - request.user.date_joined
    recent_logins = request.user.last_login and request.user.last_login >= timezone.now() - timedelta(days=7)
    user_reviewed_posts_count = Comment.objects.filter(author=request.user).values('content').distinct().count()

    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    
    if request.method == 'POST':
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_contents_count': user_contents_count,
        'user_comments_count': user_comments_count,
        'user_likes_count': user_likes_count,
        'user_registration_duration': user_registration_duration,
        'user_recent_logins': recent_logins,
        'user_reviewed_posts_count': user_reviewed_posts_count,
        'ads_base': ads_base,
    }

    return render(request, 'accounts/profile.html', context)


@login_required
def password_change(request):
    ads_base = Ad.objects.filter(placement__name="Base", active=True).first()
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form, 'ads_base': ads_base,})