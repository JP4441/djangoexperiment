from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Finch, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view

# /templates/main_app/finch_form.html

class FinchCreate(LoginRequiredMixin, CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age', 'image']
  # success_url = '/finchs/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)##superclass is Create view. 

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def finchs_index(request):
  finchs = Finch.objects.filter(user = request.user)
  return render(request, 'finchs/index.html', { 'finchs': finchs })

@login_required
def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)

  toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'finchs/detail.html', {'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have})

@login_required
def add_feeding(request, finch_id):
  print(request.POST)
  form = FeedingForm(request.POST)
  if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.finch_id = finch_id
      new_feeding.save()
  return redirect('detail', finch_id = finch_id)

class FinchUpdate(LoginRequiredMixin, UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(LoginRequiredMixin, DeleteView):
  model = Finch
  success_url = '/finchs/'

###These are classes for TOYS view etc all created by the django framework

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name','color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id = finch_id)

@login_required
def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id = finch_id)

def signup(request):
  error_message = ''
  if request.method == 'POST': 
    form = UserCreationForm(request.POST)
    if form.is_valid():
      #save user to the database
      user = form.save()
      #login user straight in
      login(request, user)
      return redirect('index')
    else:
      error_message = "Invalid signup = try again"
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)