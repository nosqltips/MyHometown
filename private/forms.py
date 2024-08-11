from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, ButtonHolder, Submit
from common.models import Event, CRCClass, CRCRegister, Project, TimeTrack

class BrowserDateInput(forms.widgets.DateInput):
    input_type = 'date'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('department', 'profile_picture', 'is_missionary')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user_profile_form'
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            Fieldset(
                'Profile',
                Field('department'),
                Field('profile_picture'),
                Field('is_missionary')
            ),
            ButtonHolder(
                Submit('submit', 'Save Changes')
            )
        )

class RegistrationForm(UserCreationForm):
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
        fields = ['profile_picture']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'time', 'location', 'url', 'summary', 'description']
        widgets = {
            "description": CKEditorWidget(),
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
            "description": CKEditorWidget(),
        }
        labels = {
            "title": _("Title of CRC Class"),
            "time": _("Dates and times that CRC class will take place"),
            "location": _("Where will this CRC class take place?"),
            "summary": _("Summary of the CRC Class"),
            "description": _("Description of the CRC Class")
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

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'date', 'time', 'location', 'url', 'summary', 'description']
        widgets = {
            "description": CKEditorWidget(),
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

class TimeTrackForm(forms.ModelForm):
    class Meta:
        model = TimeTrack
        fields = ['location', 'date', 'crc', 'service', 'other']
        widgets = {
            "date": BrowserDateInput(),
        }
        labels = {
            "location": _("Location of Hours"),
            "date": _("Date of Hours"),
            "crc": _("CRC Hours"),
            "service": _("Service Hours"),
            "other": _("Any Other Hours")
        }

