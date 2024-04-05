# app/main/urls.py

# Django and thirt party modules
from django.urls import path

# Locals
from app.main.views import *

# namespace
app_name = "main"

urlpatterns = [
    path("", home_view, name="home"),
]
