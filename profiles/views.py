from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .models import User
from .forms import SignUpForm
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import AuthenticationForm
import json
from dealer.views import deshboard
from django.http import JsonResponse

# Create your views here.
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

    
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(loginView)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def check_user_exists(request):
    uname = request.GET.get('uname')
    check = User.objects.filter(username__iexact=uname).exists()
    exists = {
        'status': check
    }
    return JsonResponse(exists, safe=False)

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_superuser:
                return redirect('index.html')

            elif request.user.user_type == 'dealer':
                return redirect(deshboard)
            else:
                return render(request,'index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request,'index.html')
