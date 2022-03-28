from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Finch


# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# finchs = [
#   Finch('Birdie', 'blue', 'always biting', 3),
#   Finch('Flyee', 'red', 'large beak', 0),
#   Finch('Raven', 'black', '3 legged finch', 4)
# ]

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


