from django.urls import path
from .views import EventListView, EventDetailView
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.home, name="public-home"),
    path('about/', views.about, name="public-about"),
    path('event/', EventListView.as_view(), name="public-events-list"),
    path('event/<int:pk>/', EventDetailView.as_view(), name="public-event-detail"),
]