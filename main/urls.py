from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /login/
    path('login/', views.login_page, name='login'),
    # ex: /register/
    path('register/', views.register, name='register'),
    # ex: /logout/
    path('logout/', views.logout_page, name='logout')
]