from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import TripForm, CreateUserForm
from .models import Trip


# Create your views here.
def userSuccess(request):
    context = {}

    return render(request, "trip_planner/loginsuccess.html", context)

def userRegister(request):
    form = CreateUserForm

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        print(request.POST)       
        print(CreateUserForm.hidden_fields)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "trip_planner/register.html", context)


def userLogin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
        print(request.GET)
        # print(form.get_user)
        # return redirect('success')
    context = {}
    return render(request, "trip_planner/login.html", context)

def userLogout(request):
    logout(request)
    return redirect('login')

class TripListView(ListView):
    model = Trip
    template_name = "tripspage.html"
    context = {}
    

class TripView(ListView):
    model = Trip
    template_name = "trip_list.html"

def tripTest(request):
    context = {}
    return render(request, "trip_planner/tripspage.html", context)

def index(request):
    form = TripForm()
    if request.method == "POST":
        print(request.POST)
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {"form": form}
    return render(request, "trip_planner/index.html", context)
