# core/context_processors.py
from .models import StaticPage, SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()
    return {
        'static_pages': StaticPage.objects.all(),
        'settings': settings,
    }
