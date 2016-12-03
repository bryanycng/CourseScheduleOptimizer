from django.shortcuts import render, HttpResponse
from django.template import loader
import requests

# Create your views here.
def index(request):
    return render(request, 'scheduler/index.html')