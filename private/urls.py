from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from .views import CRCClassListView, CRCClassDetailView, CRCClassCreateView, CRCClassUpdateView, CRCClassDeleteView, CRCClassRegistrationView, CRCClassRegistrationDeleteView
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from .views import TimeListView, TimeCreateView, TimeDeleteView, ProfileUpdateView, ProfileListView
from .views import MonthlyReportView, VolunteerReportView, export_to_csv
from django.urls import path
from . import views
from . import qr_codes

# URLConf
urlpatterns = [
    path('', views.home, name="home"),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='home', template_name='users/logout.html'), name='logout'),
    path('register', views.register, name='register'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profiles/', views.ProfileListView.as_view(template_name='users/profile_list.html'), name='profile-list'),
    path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view(template_name='users/profile_update.html'), name='profile-update'),
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
    path('crcclass/<int:pk>/register', CRCClassRegistrationView.as_view(), name="crcclass-register"),
    path('crcclass/<int:pk>/register/delete', CRCClassRegistrationDeleteView.as_view(), name="crcclass-delete"),

    path('project/', ProjectListView.as_view(), name="project-list"),
    path('projects/', ProjectListView.as_view(), name="project-list"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name="project-detail"),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name="project-update"),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name="project-delete"),
    path('projects/new/', ProjectCreateView.as_view(), name="project-create"),

    path('time/', TimeListView.as_view(), name="time-list"),
    path('time/new/', TimeCreateView.as_view(), name="time-create"),
    path('time/<int:pk>/delete', TimeDeleteView.as_view(), name="time-delete"),

    path('report/monthly', MonthlyReportView.as_view(), name="monthly-report"),
    path('report/volunteer', VolunteerReportView.as_view(), name="volunteer-report"),
    path('export_to_csv/', export_to_csv, name='export_to_csv'),

    # QR Codes
    path('qr_code/event/<pk>/', qr_codes.event_code, name='event-code'),
    path('qr_code/project/<pk>/', qr_codes.project_code, name='project-code'),
    path('qr_code/crcclass/<pk>/', qr_codes.crcclass_code, name='crcclass-code'),
]
    # path("ckeditor5/", include('django_ckeditor_5.urls')),
    # path("upload/", custom_upload_function, name="custom_upload_file"),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
