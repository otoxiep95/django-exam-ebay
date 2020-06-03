from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.models import User, Group
from .models import Profile, PasswordResetRequest
from eshop.models import ShoppingCart
from django.http import HttpResponseRedirect
import django_rq
from . messaging import email_message
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


@login_required
def logout(request):
    dj_logout(request)
    return render(request, 'accounts/login.html')


def sign_up(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_name = request.POST['user']
        email = request.POST['email']
        phone = request.POST['phone']
        group = request.POST['group']

        if password == confirm_password:
            if User.objects.create_user(user_name, email, password):
                user = get_object_or_404(User, username=user_name)
                if group == "customer":
                    user.groups.add(2)
                elif group == "seller":
                    user.groups.add(1)
                ShoppingCart.objects.create(buyer=user)
                user.profile.phone = phone
                user.profile.save()

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


@login_required
def user_profile(request):
    group = request.user.groups.all()[0].name
    context = {'group': group}
    print(group)
    return render(request, 'accounts/user_profile.html', context)


def delete_account(request):
    if request.method == "POST":
        if request.POST['confirm_delete'] == 'DELETE':
            user = authenticate(
                request, username=request.user.username, password=request.POST['password'])
            if user:
                print(f"setting user to unactive {user}")
                user.is_active = False
                user.save()
                return HttpResponseRedirect(reverse('accounts:login'))
            else:
                print("failed delete")
    return render(request, 'accounts/delete_account.html')


def request_password_reset(request):
    if request.method == "POST":
        post_user = request.POST['username']
        user = None

        if post_user:
            try:
                user = User.objects.get(username=post_user)
            except:
                print(f"Invalid password request: {post_user}")
        else:
            post_user = request.POST['email']
            try:
                user = User.objects.get(email=post_user)
            except:
                print(f"Invalid password request: {post_user}")
        if user:
            prr = PasswordResetRequest()
            prr.user = user
            prr.save()
            django_rq.enqueue(email_message, {
                'token': prr.token,
                'email': prr.user.email,
            })
            return HttpResponseRedirect(reverse('accounts:password_reset'))

    return render(request, 'accounts/request_password_reset.html')
    # if request.method == "POST":
    #     post_user = request.POST['username']
    #     user = None
    #     if post_user:
    #         try:
    #             user = User.objects.get(username=post_user)
    #         except:
    #             print(f'Invalid password: {post_user}')
    #     else:
    #         post_user = request.POST['email']
    #         try:
    #             user = User.objects.get(email=post_user)
    #         except:
    #             print(f'Invalid password: {post_user}')
    #     if user:
    #         prr = PasswordResetRequest()
    #         prr.user = user
    #         prr.save()
    #         print(prr)
    #         return HttpResponseRedirect(reverse('accounts:password_reset'))
    # return render(request, 'accounts/request_password_reset.html')


def password_reset(request):
    if request.method == "POST":
        post_user = request.POST['username']
        password = request.POST['password']
        confirm_passowrd = request.POST['confirm_password']
        token = request.POST['token']
        if password == confirm_passowrd:
            try:
                prr = PasswordResetRequest.objects.get(token=token)
                prr.save()
            except:
                print("Invalid password reset attempt")
                return render(request, 'accounts/password_reset.html')
            user = prr.user
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    return render(request, 'accounts/password_reset.html')
