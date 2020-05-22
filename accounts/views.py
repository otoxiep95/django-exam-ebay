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
    pass

def user_profile(request):
    pass

def delete_account(request):
    pass

def request_password_reset(request):
    pass

def password_reset(request):
    pass
