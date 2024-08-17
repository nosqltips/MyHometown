from django.urls import path
from .views import EventListView, EventDetailView
from .views import CRCClassListView, CRCClassDetailView, CRCClassRegistrationView, CRCClassRegistrationCompleteView
from .views import ProjectListView, ProjectDetailView
from . import views
from . import qr_codes

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.home, name="public-home"),
    path('about/', views.about, name="public-about"),

    path('event/', EventListView.as_view(), name="public-event-list"),
    path('event/<int:pk>/', EventDetailView.as_view(), name="public-event-detail"),

    path('crcclass/',  CRCClassListView.as_view(), name="public-crcclass-list"),
    path('crcclass/<int:pk>/', CRCClassDetailView.as_view(), name="public-crcclass-detail"),
    path('crcclass/<int:pk>/register', CRCClassRegistrationView.as_view(), name="public-crcclass-register"),
    path('crcclass/<int:pk>/register/complete', CRCClassRegistrationCompleteView.as_view(), name="public-crcclass-register-complete"),

    path('project/', ProjectListView.as_view(), name="public-project-list"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name="public-project-detail"),

    # QR Codes
    path('qr_code/event/<pk>/', qr_codes.event_code, name='public-event-code'),
    path('qr_code/project/<pk>/', qr_codes.project_code, name='public-project-code'),
    path('qr_code/crcclass/<pk>/', qr_codes.crcclass_code, name='public-crcclass-code'),
]