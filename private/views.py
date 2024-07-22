from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
from django.db.models import Avg, Sum, Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from .forms import MissionaryRegistrationForm, EventForm, CRCClassForm, ProjectForm, CRCRegistrationForm, TimeTrackForm
from common.models import Event, CRCClass, Project, CRCRegister, TimeTrack

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

# TIME TRACKING
class TimeListView(ListView):
    model = TimeTrack
    template_name = 'time/time_list.html'
    context_object_name = 'times'
    ordering = ['-date', '-date_posted']    

class TimeCreateView(LoginRequiredMixin, CreateView):
    model = TimeTrack
    form_class = TimeTrackForm
    template_name = 'time/time_create.html'
    context_object_name = 'time'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TimeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TimeTrack
    success_url = '/private/time'
    template_name = 'time/time_delete.html'
    context_object_name = 'time'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False


def aggregate_by_month():
    today = datetime.today()
    three_months_ago = today - timedelta(days=90)

    report_data = []
    for month in range((today.month - 1) - 2, today.month + 1):
        if month < 1:
            month += 12
            year = today.year - 1
        else:
            year = today.year

        start_date = datetime(year, month, 1)
        end_date = datetime(year, month + 1, 1) if month != 12 else datetime(year + 1, 1, 1)

        time_tracks = TimeTrack.objects.filter(date__gte=start_date, date__lt=end_date)
        total_crc = time_tracks.aggregate(total_crc=Sum('crc'))['total_crc'] or 0
        total_service = time_tracks.aggregate(total_service=Sum('service'))['total_service'] or 0
        total_other = time_tracks.aggregate(total_other=Sum('other'))['total_other'] or 0

        report_data.append({
            'month': month,
            'year': year,
            'total_crc': total_crc,
            'total_service': total_service,
            'total_other': total_other
        })

    return report_data

# Method to produce a report from TimeTrack model to aggregate by month
class MonthlyReportView(ListView):
    model = TimeTrack
    template_name = 'reports/monthly_report.html'
    context_object_name = 'report_data'

    def get_queryset(self):
        return aggregate_by_month()


# Method to produce a report from TimeTrack model to aggregate by month
class VolunteerReportView(ListView):
    model = TimeTrack
    template_name = 'reports/volunteer_report.html'
    context_object_name = 'report_data'

    def get_queryset(self):
        # Aggregate the float fields by user for the last 30 days
        thirty_days_ago = datetime.now() - timedelta(days=30)
        aggregates = (TimeTrack.objects
                        .filter(date__gte=thirty_days_ago)
                        .values('author').annotate(
                            crc_sum=Sum('crc'), 
                            service_sum=Sum('service'), 
                            other_sum=Sum('other')
                        )
                    )
                    
        return aggregates
