from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
import calendar
import csv
from django.urls import reverse_lazy, resolve
from django.http import HttpResponse, Http404
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from .forms import UserRegisterForm, UserUpdateForm, ProfileForm, ProfileUpdateForm
from .forms import EventForm, CRCClassForm, ProjectForm, CRCRegistrationForm, TimeTrackForm
from common.models import Event, CRCClass, Project, CRCRegister, TimeTrack
from .models import Profile

def home(request):
    return render(request, 'private/index.html')

def about(request):
    return render(request, 'private/about.html')

@login_required
def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_uupdate(request, pk):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, f'Your account has been updated.')
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'users/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/profile_update.html'

    def get_object(self):
        try:
            return Profile.objects.get(pk=self.kwargs['pk'])
        except Profile.DoesNotExist:
            raise Http404('Profile not found')

    def get_success_url(self):
        pk = self.object.pk
        return reverse('profile', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        profile = self.get_object()
        context['user_form'] = UserUpdateForm(instance=profile.user)
        context['profile_form'] = ProfileUpdateForm(instance=profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = self.get_form()
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.save(commit=False)
            profile_form.instance.user = user
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect(reverse('profile', args=[self.object.pk]))
        else:
            return self.render_to_response(self.get_context_data(user_form=user_form, profile_form=profile_form))

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'users/profile_list.html'
    context_object_name = 'profiles'
    ordering = ['user_id']  


# EVENTS
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['date_posted']    

class EventDetailView(LoginRequiredMixin, DetailView):
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
        if self.request.user == event.author or self.request.user.is_staff:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/private/event'
    template_name = 'events/event_delete.html'
    context_object_name = 'event'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author or self.request.user.is_staff:
            return True
        return False

# CRC CLASSES
class CRCClassListView(LoginRequiredMixin, ListView):
    model = CRCClass
    template_name = 'crcclasses/crcclass_list.html'
    context_object_name = 'crcclasses'
    ordering = ['date_posted']    

class CRCClassDetailView(LoginRequiredMixin, DetailView):
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
        if self.request.user == event.author or self.request.user.is_staff:
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
        if self.request.user == event.author or self.request.user.is_staff:
            return True
        return False

class CRCClassRegistrationView(LoginRequiredMixin, CreateView):
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
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    ordering = ['date_posted']    

class ProjectDetailView(LoginRequiredMixin, DetailView):
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
        if self.request.user == project.author or self.request.user.is_staff:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/private/project'
    template_name = 'projects/project_delete.html'
    context_object_name = 'project'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author or self.request.user.is_staff:
            return True
        return False

# TIME TRACKING
class TimeListView(LoginRequiredMixin, ListView):
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
        if self.request.user == project.author or self.request.user.is_staff:
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

        month_name = calendar.month_name[month]
        report_data.append({
            'month': month_name,
            'year': year,
            'total_crc': total_crc,
            'total_service': total_service,
            'total_other': total_other
        })

    return report_data

# Method to produce a report from TimeTrack model to aggregate by month
class MonthlyReportView(LoginRequiredMixin, ListView):
    model = TimeTrack
    template_name = 'reports/monthly_report.html'
    context_object_name = 'report_data'

    def get_queryset(self):
        return aggregate_by_month()

def export_to_csv(request):
    # Call the existing method to generate the data
    data = aggregate_by_month()

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="monthly_report.csv"'

    # Write the CSV data to the response
    writer = csv.DictWriter(response, fieldnames=['month', 'year', 'total_crc', 'total_service', 'total_other'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

    return response

# Method to produce a report from TimeTrack model to aggregate by month
class VolunteerReportView(LoginRequiredMixin, ListView):
    model = TimeTrack
    template_name = 'reports/volunteer_report.html'
    context_object_name = 'report_data'

    def get_queryset(self):
        # Aggregate the float fields by user for the last 30 days
        thirty_days_ago = datetime.now() - timedelta(days=30)
        aggregates = (TimeTrack.objects
                        .filter(date__gte=thirty_days_ago)
                        .annotate(author_username=F('author__username'))  # Add this line
                        .values('author_username')  # Update this line
                        .annotate(
                            crc_sum=Sum('crc'), 
                            service_sum=Sum('service'), 
                            other_sum=Sum('other')
                        )
                    )
                    
        return aggregates
