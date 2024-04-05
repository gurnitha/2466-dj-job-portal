# app/main/views.py

# Django and third party modules
from django.shortcuts import render

# Create your views here.

def home_view(request):
	return render(request, 'main/index.html')
