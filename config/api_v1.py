from django.urls import path, include

urlpatterns = [
    path('verf/', include('verf.urls')),
    path('profile/', include('user_profile.urls')),
]
