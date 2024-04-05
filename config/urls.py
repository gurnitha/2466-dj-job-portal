# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # app/main
    path("", include("app.main.urls", namespace="main")),
]
