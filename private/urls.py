from django.contrib.auth import views as auth_views
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home, name="home"),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name="about"),

    path('event/', EventListView.as_view(), name="event-list"),
    path('events/', EventListView.as_view(), name="event-list"),
    path('event/<int:pk>/', EventDetailView.as_view(), name="event-detail"),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name="event-update"),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name="event-delete"),
    path('event/new/', EventCreateView.as_view(), name="event-create")
]
