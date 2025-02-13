from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]

if DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
