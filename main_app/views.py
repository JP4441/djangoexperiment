from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Finch
from django.views.generic.edit import CreateView

# Define the home view

# /templates/main_app/finch_form.html

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  # success_url = '/finchs/'

def home(request):
  return render(request, 'home.html')  

def about(request):
  return render(request, 'about.html')

def finchs_index(request):
  finchs = Finch.objects.all()
  return render(request, 'finchs/index.html', { 'finchs': finchs })

def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finchs/detail.html', {'finch': finch})




