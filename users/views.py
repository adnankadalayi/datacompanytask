from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import UserRegistrationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, City


def home(request):
    
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    person = Person.objects.all()
    
    context = {
        'form': form,
        'person': person,
    }
    return render(request, 'home.html', context)


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return JsonResponse(list(cities.values('id', 'name')), safe=False)

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        print('post')
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)	
            return redirect('home')    
    return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')