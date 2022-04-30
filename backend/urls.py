from django.urls import path
from . import views 

urlpatterns = [
    path('public_book_data', views.public_book_data, name="public_book_data"),
   
]