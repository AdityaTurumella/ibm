from django.contrib.auth import views
from django.urls import path,include
from .import views

app_name = 'main' 
urlpatterns = [
    path('video/',views.video,name='video'),
    path('',views.home,name='home'),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("about/", views.about, name="about"),
]