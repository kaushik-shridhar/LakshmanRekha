"""LakshmanRekha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ex: localhost:8000/
    path('', include('home.urls')),
    # ex: localhost:8000/geofence/
    path('geofence/', include('geofence.urls')),
    # ex: localhost:8000/tracking/
    path('tracking/', include('tracking.urls')),
    # ex: localhost:8000/admin/
    path('admin/', admin.site.urls),
]
