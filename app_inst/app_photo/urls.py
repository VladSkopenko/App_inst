from django.contrib import admin
from django.urls import path
from . import views

app_name = "app_photo"  # название переменной обяхательно должно быть app_name
urlpatterns = [
    path("", views.index, name="home"),
    path("images/", views.pictures, name="pictures"),
    path("upload/", views.upload, name="upload"),  # app_photo:home
]
