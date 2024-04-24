from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy
from django.views.generic.edit import CreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:home')
        ),
        name='registration'
    ),
    path('', include('pages.urls', namespace='pages')),
    path('cats/', include('cats.urls', namespace='cat')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
