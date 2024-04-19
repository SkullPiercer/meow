from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cat'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('categories', views.categories, name='categories')
]
