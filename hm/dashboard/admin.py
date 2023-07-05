from django.contrib import admin

from dashboard.models import Ailment, Appointment


# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Ailment)
class AilmentAdmin(admin.ModelAdmin):
    pass
