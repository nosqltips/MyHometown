from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from .forms import MissionaryRegistrationForm, EventForm, CRCClassForm, ProjectForm
from common.models import Event, CRCClass, Project

def home(request):
    return render(request, 'private/index.html')

def about(request):
    return render(request, 'private/about.html')

def register(request):
    if request.method == 'POST':
        form = MissionaryRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.clean_password.get('username')
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')

    else:
        form = MissionaryRegistrationForm()
        return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# EVENTS
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['date_posted']    

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_create.html'
    context_object_name = 'event'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_update.html'
    context_object_name = 'event'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/private/event'
    template_name = 'events/event_delete.html'
    context_object_name = 'event'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

# CRC CLASSES
class CRCClassListView(ListView):
    model = CRCClass
    template_name = 'crcclasses/crcclass_list.html'
    context_object_name = 'crcclasses'
    ordering = ['date_posted']    

class CRCClassDetailView(DetailView):
    model = CRCClass
    template_name = 'crcclasses/crcclass_detail.html'
    context_object_name = 'crcclass'

class CRCClassCreateView(LoginRequiredMixin, CreateView):
    model = CRCClass
    form_class = CRCClassForm
    template_name = 'crcclasses/crcclass_create.html'
    context_object_name = 'crcclass'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CRCClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CRCClass
    form_class = CRCClassForm
    template_name = 'crcclasses/crcclass_update.html'
    context_object_name = 'crcclass'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

# Do we delete or disable?
# What about class registrations?
class CRCClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CRCClass
    success_url = '/private/class'
    template_name = 'crcclasses/crcclass_delete.html'
    context_object_name = 'crcclass'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


# PROJECTS
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    ordering = ['date_posted']    

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'
    context_object_name = 'project'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_update.html'
    context_object_name = 'project'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/private/project'
    template_name = 'projects/project_delete.html'
    context_object_name = 'project'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

# def events(request):
#     context = {
#         'events': Event.objects.all()
#     }
#     return render(request, 'events/events.html', context)
