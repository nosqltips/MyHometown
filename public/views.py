from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from common.models import Event, CRCClass, Project, CRCRegister
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView
from .forms import CRCRegistrationForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crcclass_id = self.kwargs['pk']
        crcclass = CRCClass.objects.filter(id=crcclass_id).first()
        context['crcclass'] = crcclass
        context['registrations'] = CRCRegister.objects.filter(crcclass=crcclass)
        return context
    
class CRCClassRegistrationView(CreateView):
    model = CRCRegister
    form_class = CRCRegistrationForm
    template_name = 'public_crcclasses/crcclass_registration.html'
    context_object_name = 'crcregister'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crcclass_id = self.kwargs['pk']
        context['crcclass_id'] = crcclass_id
        return context

    def form_valid(self, form):
        id = self.kwargs['pk']
        form.instance.crcclass_id = id
        super().form_valid(form)
        object = self.object
        url = reverse('public-crcclass-register-complete', kwargs={'pk': object.pk})
        return HttpResponseRedirect(url)

class CRCClassRegistrationCompleteView(TemplateView):
    template_name = 'public_crcclasses/crcclass_registration_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crcregister_id = self.kwargs['pk']
        registration = CRCRegister.objects.filter(id=crcregister_id).first()
        context['registration'] = registration
        return context

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

