from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscription
from .forms import SubscriptionForm

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
