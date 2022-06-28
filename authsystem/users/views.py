from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User_profile
from .forms import setGoalsForm

# from authsystem.users.models import Profile

from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'User_profile': User_profile})

def setgoals(request):
    form2 = setGoalsForm(request.POST)
    return render(request, 'users/setgoals.html', {'form': form2})
    if request == "POST":
        form2 = setGoalsForm(request.POST)
        if form2.is_valid():
            form2.save()
            username = form2.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your goals have been successfully set')


