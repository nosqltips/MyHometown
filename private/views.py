from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MissionaryRegistrationForm

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def register(request):
    if request.method == 'POST':
        form = MissionaryRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.clean_password.get('username')
            messages.success(request, f'Your account has been create! You can no log in.')
            return redirect('login')

    else:
        form = MissionaryRegistrationForm()
        return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')