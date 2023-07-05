from django.contrib import admin

from user_auth.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
