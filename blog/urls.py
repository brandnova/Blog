from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)