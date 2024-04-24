from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('pages.urls', namespace='pages')),
    path('cats/', include('cats.urls', namespace='cat')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
