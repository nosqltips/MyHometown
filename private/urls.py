from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="private-home"),
    path('about', views.about, name="private-about"),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    # path('login', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
