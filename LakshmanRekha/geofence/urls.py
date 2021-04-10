from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /geofence/
    path('', views.index, name='index'),
    # ex: /geofence/success/
    path('success/', views.success, name='success'),
    # ex: /geofence/display_maps/
    path('display_maps/', views.display_map_images, name='display_maps'),
    # ex: /geofence/create_geofence/
    path('create_geofence/', views.create_geofence, name='create_geofence'),
    # ex: /geofence/delete_geofence/
    path('delete_geofence/', views.delete_geofence, name='delete_geofence'),
    # ex: /geofence/my_view_that_sends_coordinates/
    path('my_view_that_sends_coordinates/', views.my_view_that_sends_coordinates, name='my_view_that_sends_coordinates'),
    # ex: /geofence/add_ap/
    path('add_ap/', views.add_ap, name='add_ap'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)