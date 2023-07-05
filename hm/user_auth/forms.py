from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_auth.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')