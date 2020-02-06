
from django.contrib import admin
from django.urls import path
#   from .views import AboutmeListView
from . import views 



urlpatterns = [
    path('' , views.index, name="index"),
   
   
]
