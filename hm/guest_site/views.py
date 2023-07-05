from django.shortcuts import render
from django.http import HttpResponse

from user_auth.models import User

# Create your views here.
def home(request):
    doctors = User.objects.filter(staff_type='doctor')
    context = {
        'doctors': doctors
    }
    return render(request, 'guest_site/index.html', context)