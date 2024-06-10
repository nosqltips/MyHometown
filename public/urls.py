from django.urls import path
from .views import EventListView, EventDetailView
from .views import ClassListView, ClassDetailView
from .views import ProjectListView, ProjectDetailView
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.home, name="public-home"),
    path('about/', views.about, name="public-about"),

    path('event/', EventListView.as_view(), name="public-event-list"),
    path('event/<int:pk>/', EventDetailView.as_view(), name="public-event-detail"),

    path('class/',  ClassListView.as_view(), name="public-class-list"),
    path('class/<int:pk>/', ClassDetailView.as_view(), name="public-class-detail"),

    path('project/', ProjectListView.as_view(), name="public-project-list"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name="public-project-detail"),
]