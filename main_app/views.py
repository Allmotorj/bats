from django.shortcuts import render, redirect
from . models import Bat, Toy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class BatCreate(LoginRequiredMixin, CreateView):
    model = Bat
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BatUpdate(LoginRequiredMixin, UpdateView):
    model = Bat
    fields = ['breed', 'description', 'age']

class BatDelete(LoginRequiredMixin, DeleteView):
    model = Bat
    success_url = '/bats/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def bats_index(request):
    bats = Bat.objects.filter(user = request.user)
    return render(request, 'bats/index.html', { 'bats': bats })

@login_required
def bats_detail(request, bat_id):
    bat = Bat.objects.get(id=bat_id)
    toys_bat_doesnt_have = Toy.objects.exclude(id__in = bat.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'bats/detail.html', {
        'bat': bat, 
        'feeding_form': feeding_form,
        'toys': toys_bat_doesnt_have
    })

@login_required
def add_feeding(request, bat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bat_id = bat_id 
        new_feeding.save()
    return redirect('detail', bat_id=bat_id)

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

@login_required
def assoc_toy(request, bat_id, toy_id):
    bat = Bat.objects.get(id=bat_id)
    bat.toys.add(toy_id)
    return redirect('detail', bat_id=bat_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)