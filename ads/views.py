from datetime import timezone
from django.shortcuts import render
from .models import AdPlacement

def get_ads_context():
    ads = {}
    placements = AdPlacement.objects.filter(active=True)
    for placement in placements:
        active_ads = placement.ads.filter(active=True, start_date__lte=timezone.now(), end_date__gte=timezone.now())
        if active_ads.exists():
            ads[placement.slug] = active_ads.first().code
    return ads

def ads_render(request):
    context = get_ads_context()
    # Add other context variables as needed
    return render(request, 'some_template.html', context)
