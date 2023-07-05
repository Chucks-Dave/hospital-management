from django.shortcuts import render, redirect
from dashboard.models import Ailment, Appointment
from user_auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import random


# Create your views here.
@login_required
def patient_dashboard(request, username):
    page = request.GET.get('page')
    appointments = request.user.appointments.all().order_by('-date')
    
    appointment_summary = Paginator(appointments, 2).get_page(page)
    
    doctors = User.objects.filter(staff_type="doctor")
    
    ailments = Ailment.objects.all()
    i = 1
    infection_today = ailments.first()
    while not i == 0:
        random_ailment = random.randint(1, ailments.count() + 1)
        
        if ailments.filter(id=random_ailment).exists():
            infection_today = Ailment.objects.get(id=random_ailment)
            break;
        
    
    context = {
        'appointment_summary': appointment_summary,
        'appointments': appointments,
        'doctors': doctors,
        'ailments': ailments,
        'infection_today': infection_today,
    }

    return render(request, 'dashboard/patient/home.html', context)


@login_required
def create_appointment(request):
    if request.method == "POST":
        doctor = request.POST['doctor']
        reason = request.POST['reason']
        date = request.POST['date']
        time = request.POST['time']
        client = request.user
        
        Appointment(doctor=User.objects.get(pk=doctor), reason=reason, date=date, time=time, client=client).save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('patient_dashboard', request.user.username)


@login_required
def reschedule_appointment(request, pk):
    if request.method == "POST":
        date = request.POST['edit_date']
        time = request.POST['edit_time']
        
        appointment = Appointment.objects.get(pk=pk)
        appointment.date = date
        appointment.time = time
        appointment.save()
        
    return redirect('patient_dashboard', request.user.username)


@login_required
def doctor_dashboard(request, username):
    context = {}

    return render(request, 'dashboard/doctor/home.html', context)
