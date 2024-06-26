from django.contrib.auth import views as auth_views
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from .views import CRCClassListView, CRCClassDetailView, CRCClassCreateView, CRCClassUpdateView, CRCClassDeleteView
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
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
    path('event/new/', EventCreateView.as_view(), name="event-create"),

    path('crcclass/', CRCClassListView.as_view(), name="crcclass-list"),
    path('crcclasses/', CRCClassListView.as_view(), name="crcclass-list"),
    path('crcclass/<int:pk>/', CRCClassDetailView.as_view(), name="crcclass-detail"),
    path('crcclass/<int:pk>/update', CRCClassUpdateView.as_view(), name="crcclass-update"),
    path('crcclass/<int:pk>/delete', CRCClassDeleteView.as_view(), name="crcclass-delete"),
    path('crcclass/new/', CRCClassCreateView.as_view(), name="crcclass-create"),

    path('project/', ProjectListView.as_view(), name="project-list"),
    path('projects/', ProjectListView.as_view(), name="project-list"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name="project-detail"),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name="project-update"),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name="project-delete"),
    path('claprojectss/new/', ProjectCreateView.as_view(), name="project-create")
]
