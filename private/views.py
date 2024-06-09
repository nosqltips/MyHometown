from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import MissionaryRegistrationForm
from common.models import Event, Class, Project

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
    fields = ['title', 'time', 'location', 'url', 'description']
    template_name = 'events/event_create.html'
    context_object_name = 'event'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'time', 'location', 'url', 'description']
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

# CLASSES
class ClassListView(ListView):
    model = Class
    template_name = 'classes/class_list.html'
    context_object_name = 'classes'
    ordering = ['date_posted']    

class ClassDetailView(DetailView):
    model = Class
    template_name = 'classes/class_detail.html'
    context_object_name = 'class'

class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    fields = ['title', 'location', 'times', 'description']
    template_name = 'classes/class_create.html'
    context_object_name = 'class'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Class
    fields = ['title', 'location', 'times', 'description']
    template_name = 'classes/class_update.html'
    context_object_name = 'class'

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
class ClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Class
    success_url = '/private/class'
    template_name = 'classes/class_delete.html'
    context_object_name = 'class'

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
    fields = ['title', 'time', 'location', 'url', 'description']
    template_name = 'projects/project_create.html'
    context_object_name = 'project'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'time', 'location', 'url', 'description']
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
