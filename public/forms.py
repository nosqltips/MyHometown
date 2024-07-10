from django import forms
from django.utils.translation import gettext_lazy as _
from common.models import CRCRegister

class CRCRegistrationForm(forms.ModelForm):
    class Meta:
        model = CRCRegister

        fields = ['name', 'phone', 'email']
        labels = {
            "name": _("Name of person registering for this CRC class"),
            "phone": _("Phone number"),
            "email": _("Email address")
        }