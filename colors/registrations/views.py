from django.shortcuts import render

# Create your views here.
from .forms import UserProfileForm
from django.views.generic import TemplateView, CreateView, FormView, ListView
from django.urls import reverse_lazy, reverse
from .models import UserProfile


class RegistrationsFormView(CreateView):
    template_name = "index.html"
    form_class = UserProfileForm
    success_url = reverse_lazy('registrations:index')


class ReportView(ListView):
    context_object_name = 'registrationList'
    model = UserProfile
    template_name = "reports.html"
