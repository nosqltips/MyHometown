from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from common.models import Event, CRCClass, CRCRegister, Project

class BrowserDateInput(forms.widgets.DateInput):
    input_type = 'date'

class MissionaryRegistrationForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'time', 'location', 'url', 'summary', 'description']
        widgets = {
            "description": forms.Textarea(attrs={"cols": 80, "rows": 5}),
            "date": BrowserDateInput(),
            "time": forms.TimeInput
        }
        labels = {
            "title": _("Title of Event"),
            "date": _("Date of Event"),
            "time": _("Time of Event"),
            "location": _("Where will this event take place?"),
            "url": _("Related URL for more information if needed."),
            "summary": _("Summary of the Event"),
            "description": _("Description of the Event")
        }

class CRCClassForm(forms.ModelForm):
    class Meta:
        model = CRCClass
        fields = ['title', 'location', 'times', 'summary', 'description']
        widgets = {
            "description": forms.Textarea(attrs={"cols": 80, "rows": 5}),
        }
        labels = {
            "title": _("Title of CRC Class"),
            "time": _("Dates and times that CRC class will take place"),
            "location": _("Where will this CRC class take place?"),
            "summary": _("Summary of the CRC Class"),
            "description": _("Description of the CRC Class")
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'date', 'time', 'location', 'url', 'summary', 'description']
        widgets = {
            "description": forms.Textarea(attrs={"cols": 80, "rows": 5}),
            "date": BrowserDateInput(),
            "time": forms.TimeInput
        }
        labels = {
            "title": _("Title of Project"),
            "date": _("Date of Project"),
            "time": _("Time of Project"),
            "location": _("Where will this project take place?"),
            "url": _("Related URL for more information if needed."),
            "summary": _("Summary of the Project"),
            "description": _("Description of the Project")
        }

class CRCRegistrationForm(forms.ModelForm):
    class Meta:
        model = CRCRegister

        fields = ['name', 'phone', 'email']
        labels = {
            "name": _("Name of person registering for this CRC class"),
            "phone": _("Phone number"),
            "email": _("Email address")
        }