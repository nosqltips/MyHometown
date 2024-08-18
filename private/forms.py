from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, ButtonHolder, Submit
from common.models import Event, CRCClass, CRCRegister, Project, TimeTrack


class BrowserDateInput(forms.widgets.DateInput):
    input_type = 'date'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('is_missionary', 'department', 'profile_picture')

        labels = {
            "is_missionary": _("Is this Volunteer a missionary"),
            "department": _("Volunteer department, usually CRC or Service"),
            "profile_picture": _("Profile Picture")
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user_profile_form'
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            HTML('<br>'),
            Field('is_missionary', css_class='form-group col-md-6'),
            Field('department', css_class='form-group col-md-6'),
            Field('profile_picture', css_class='form-group col-md-6'),
            ButtonHolder(
                Submit('submit', 'Save Changes')
            )
        )

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('department', 'profile_picture')

        labels = {
            "department": _("Volunteer department, usually CRC or Service"),
            "profile_picture": _("Profile Picture")
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user_profile_update_form'
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            HTML('<br>'),
            Field('department', css_class='form-group col-md-6'),
            Field('profile_picture', css_class='form-group col-md-6'),
            ButtonHolder(
                Submit('submit', 'Save Changes')
            )
        )

class EventForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = ['title', 'date', 'time', 'location', 'url', 'summary', 'description', 'image_file']
        widgets = {
            "description": forms.Textarea(attrs={'rows': 10, 'cols': 50}),
            "date": BrowserDateInput(),
        }
        labels = {
            "title": _("Title of Event"),
            "date": _("Date of Event"),
            "time": _("Time of Event"),
            "location": _("Where will this event take place?"),
            "url": _("Related URL for more information if needed."),
            "summary": _("Summary of the Event"),
            "description": _("Description of the Event"),
            "image_file": _("Image related to Event")
        }

class CRCClassForm(forms.ModelForm):
    class Meta:
        model = CRCClass
        fields = ['title', 'location', 'times', 'summary', 'description', 'image_file']
        widgets = {
            "description": forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        }
        labels = {
            "title": _("Title of CRC Class"),
            "time": _("Dates and times that CRC class will take place"),
            "location": _("Where will this CRC class take place?"),
            "summary": _("Summary of the CRC Class"),
            "description": _("Description of the CRC Class"),
            "image_file": _("Image related to CRC Class")
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
        fields = ['title', 'date', 'time', 'location', 'url', 'summary', 'description', 'image_file']
        widgets = {
            "description": forms.Textarea(attrs={'rows': 10, 'cols': 50}),
            "date": BrowserDateInput(),
        }
        labels = {
            "title": _("Title of Project"),
            "date": _("Date of Project"),
            "time": _("Time of Project"),
            "location": _("Where will this project take place?"),
            "url": _("Related URL for more information if needed."),
            "summary": _("Summary of the Project"),
            "description": _("Description of the Project"),
            "image_file": _("Image related to Project")
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

