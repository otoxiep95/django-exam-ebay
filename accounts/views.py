from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    context = {}

    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['user'], password=request.POST['password'])
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('eshop:index'))
        else:
            context = {
                'error': 'bad username or password'
            }

    return render(request, 'accounts/login.html', context)

def logout(request):
    pass

def sign_up(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_name = request.POST['user']
        email = request.POST['email']
        phone = request.POST['phone']
        if password == confirm_password:
            if User.objects.create_user(user_name, email, password):
                user = get_object_or_404(User, username=user_name)
               
                return HttpResponseRedirect(reverse('accounts:login'))
            else:
                context = {
                    'error': 'could not create user account'
                }
        else:
            context = {
                'error': 'passwords do not match'
            }
    return render(request, 'accounts/sign_up.html', context)

def user_profile(request):
    pass

def delete_account(request):
    pass

def request_password_reset(request):
    pass

def password_reset(request):
    pass
