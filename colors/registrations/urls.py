from django.urls import path
from .views import RegistrationsFormView,ReportView

app_name = 'registrations'
urlpatterns = [
    path('', RegistrationsFormView.as_view(), name='index'),
    path('show/', ReportView.as_view(), name='reports')
]
