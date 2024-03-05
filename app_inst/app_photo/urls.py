from django.contrib import admin
from django.urls import path
from . import views


app_name = "app_photo" # название переменной обяхательно должно быть app_name
urlpatterns = [
    path("", views.index, name="home"),   #app_photo:home
]
