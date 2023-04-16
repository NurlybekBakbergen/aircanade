from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('clogin/pages/login', csrf_exempt(views.Login.as_view()))
]
