from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
import django


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
