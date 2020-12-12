from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /register/
    path('register', views.registration, name='register'),
    # ex: /login/
    path('login', views.login, name='login'),
    # ex: /functionality
    path('functionality', views.functionality, name='functionality')
]