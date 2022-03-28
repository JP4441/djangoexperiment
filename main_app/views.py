from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Finch


# Define the home view
def home(request):
  return render(request, 'home.html')  
# def about(request):
#   return HttpResponse('<h1>About /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def finchs_index(request):
  finchs = Finch.objects.all()
  return render(request, 'finchs/index.html', { 'finchs': finchs })

def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finchs/detail.html', {'finch': finch})

