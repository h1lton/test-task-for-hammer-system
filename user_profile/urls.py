from django.urls import path

from user_profile.views import ProfileView, SetReferrerView

urlpatterns = [
    path('', ProfileView.as_view(), name='user-profile'),
    path('referrer/', SetReferrerView.as_view(), name='set-referrer'),
]
