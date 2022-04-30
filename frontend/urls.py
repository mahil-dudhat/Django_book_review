from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('public', views.public, name="public"),
    path('personal', views.personal, name="personal"),

]