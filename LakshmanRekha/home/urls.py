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
    path('logout/', views.logout_page, name='logout'),
    # ex: /functionality/
    path('functionality/', views.functionality, name='functionality'),
    # ex: /about/
    path('about/', views.about, name='about'),
    # ex: /contact_us/
    path('contact_us/', views.contact_us, name='contact_us'),
    path('return_to_home/', views.return_to_home, name='return_to_home'),
    path('patients/', views.patients, name='patients'),
]