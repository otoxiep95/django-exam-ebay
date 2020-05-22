from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('request_password_reset/', views.request_password_reset,
         name='request_password_reset'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('profile/', views.user_profile, name='user_profile')
]