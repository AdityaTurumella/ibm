
from django.contrib import admin
from django.urls import path , include
from editor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('code/',views.Edit,name='code'),



]

