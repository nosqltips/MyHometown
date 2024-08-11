from django.contrib import admin
from .models import Event, Project, CRCClass, CRCRegister
from private.models import Profile

# Register your models here.
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(CRCClass)
admin.site.register(CRCRegister)
admin.site.register(Profile)