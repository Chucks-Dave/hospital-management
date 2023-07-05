from django.urls import path

from .views import create_appointment, doctor_dashboard, patient_dashboard, reschedule_appointment

urlpatterns = [
    path('<str:username>/', patient_dashboard, name='patient_dashboard'),
    path('create_appointment', create_appointment, name='create_appointment'),
    path('reschedule/<int:pk>/', reschedule_appointment, name="reschedule"),
    
    path('doctor/<str:username>/', doctor_dashboard, name='doctor_dashboard'),
]
