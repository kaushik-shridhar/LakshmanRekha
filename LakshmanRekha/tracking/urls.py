from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /tracking/
    path('', views.index, name='index'),
    path('update/', views.update, name='update'),
    path('validate/', views.validate_patient, name='validate'),
    # path('register/', views.validate_patient, name='register'),
    path('recieve/', views.recieve, name='recieve'),
    path('sse/', views.sse, name='sse'),
    path('stream/', views.stream, name='stream'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)