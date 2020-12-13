from django.urls import path
from . import views

urlpatterns = [
    # ex: /canvas/geofence
    path('geofence', views.geofence, name='geofence'),
    path('trial', views.trial, name='trial')
]