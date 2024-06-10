from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from common.models import Event, Class, Project

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
        fields = ['title', 'date', 'time', 'location', 'url', 'description']
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
            "description": _("Description of the Event")
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['title', 'location', 'times', 'description']
        widgets = {
            "description": forms.Textarea(attrs={"cols": 80, "rows": 5}),
        }
        labels = {
            "title": _("Title of Class"),
            "time": _("Dates and times that class will take place"),
            "location": _("Where will this event take place?"),
            "description": _("Description of the Class")
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'date', 'time', 'location', 'url', 'description']
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
            "description": _("Description of the Project")
        }
