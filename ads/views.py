from datetime import timezone
from django.shortcuts import render
from .models import AdPlacement

def get_ads_context():
    ads = {}
    placements = AdPlacement.objects.filter(active=True)
    now = timezone.now().date()
    for placement in placements:
        active_ads = placement.ads.filter(active=True, start_date__lte=now, end_date__gte=now)
        if active_ads.exists():
            ads[placement.slug] = active_ads.first().code
    return ads

# def ads_render_home(request):
#     context = get_ads_context()
#     # Add other context variables as needed
#     return render(request, 'core/index.html', context)


# def ads_render_details(request):
#     context = get_ads_context()
#     return render(request, 'content/single-post.html', {'ads': context})