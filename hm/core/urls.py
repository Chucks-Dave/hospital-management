from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('', include('guest_site.urls')),
    path('dashboard/', include('dashboard.urls')),
]
