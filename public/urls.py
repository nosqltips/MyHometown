from django.urls import path
from .views import EventListView, EventDetailView
from .views import CRCClassListView, CRCClassDetailView
from .views import ProjectListView, ProjectDetailView
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.home, name="public-home"),
    path('about/', views.about, name="public-about"),

    path('event/', EventListView.as_view(), name="public-event-list"),
    path('event/<int:pk>/', EventDetailView.as_view(), name="public-event-detail"),

    path('crcclass/',  CRCClassListView.as_view(), name="public-crcclass-list"),
    path('crcclass/<int:pk>/', CRCClassDetailView.as_view(), name="public-crcclass-detail"),

    path('project/', ProjectListView.as_view(), name="public-project-list"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name="public-project-detail"),
]