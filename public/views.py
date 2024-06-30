from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from common.models import Event, CRCClass, Project
from django.views.generic import ListView, DetailView

# Create your views here.
def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Me'})

def home(request):
    return render(request, 'public/index.html')

def about(request):
    return render(request, 'public/about.html')

class EventListView(ListView):
    model = Event
    template_name = 'public_events/event_list.html'
    context_object_name = 'events'
    ordering = ['date_posted']    

class EventDetailView(DetailView):
    model = Event
    template_name = 'public_events/event_detail.html'
    context_object_name = 'event'
    
class CRCClassListView(ListView):
    model = CRCClass
    template_name = 'public_crcclasses/crcclass_list.html'
    context_object_name = 'crcclasses'
    ordering = ['date_posted']    

class CRCClassDetailView(DetailView):
    model = CRCClass
    template_name = 'public_crcclasses/crcclass_detail.html'
    context_object_name = 'crcclass'
    
class ProjectListView(ListView):
    model = Project
    template_name = 'public_projects/project_list.html'
    context_object_name = 'projects'
    ordering = ['date_posted']    

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'public_projects/project_detail.html'
    context_object_name = 'project'
    
# def events(request):
#     context = {
#         'events': Event.objects.all()
#     }
#     return render(request, 'events/events.html', context)

