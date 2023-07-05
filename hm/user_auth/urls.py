from django.urls import path

from user_auth.views import login, logout, signup

urlpatterns = [
    path('', login, name="login"),
    path('sign-up/', signup, name="signup"),
    path('logout/', logout, name="logout"),
]
