from django.urls import path, include
from django.conf.urls import url
from . import views
import django_eventstream

urlpatterns = [
    path('', views.index, name='index'),
    path('stream', views.stream, name='stream'),
    path('events/', include(django_eventstream.urls), {'channels': ['test']}),
]