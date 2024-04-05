# config/urls.py

# Django moduls
from django.contrib import admin
from django.urls import path

# Local
from app.main.views import home_view

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # app/main
    path("", home_view),
]
