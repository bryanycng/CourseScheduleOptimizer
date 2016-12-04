from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from forms import indexForm

from django import forms
import requests

# Create your views here.
def index(request):
	form_class = indexForm
	if request.method == 'POST':
		form = indexForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('result')
	return render(request, 'scheduler/index.html', {'form': form_class})

def result(request):
    return render(request, 'scheduler/result.html')