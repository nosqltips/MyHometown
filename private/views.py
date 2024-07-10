from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from .forms import MissionaryRegistrationForm, EventForm, CRCClassForm, ProjectForm, CRCRegistrationForm
from common.models import Event, CRCClass, Project, CRCRegister

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crcclass_id = self.kwargs['pk']
        crcclass = CRCClass.objects.filter(id=crcclass_id).first()
        context['crcclass'] = crcclass
        context['registrations'] = CRCRegister.objects.filter(crcclass=crcclass)
        return context
     
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
    success_url = '/private/crcclasses'
    template_name = 'crcclasses/crcclass_delete.html'
    context_object_name = 'crcclass'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class CRCClassRegistrationView(CreateView):
    model = CRCRegister
    form_class = CRCRegistrationForm
    template_name = 'crcclasses/crcclass_registration.html'
    context_object_name = 'crcregister'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crcclass_id = self.kwargs['pk']
        context['crcclass_id'] = crcclass_id
        return context

    def form_valid(self, form):
        id = self.kwargs['pk']
        crcclass = get_object_or_404(CRCClass, id)
        form.instance.crcclass = crcclass
        return super().form_valid(form)
           
class CRCClassRegistrationDeleteView(LoginRequiredMixin,  DeleteView):
    model = CRCRegister
    template_name = 'crcclasses/crcclass_registration_confirm_delete.html'
    context_object_name = 'crcregister'

    def get_success_url(self, **kwargs):
        id = self.object.crcclass.id
        return reverse('crcclass-detail', kwargs={'pk': id}) 


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
