from django.urls import path

from .views import SendCodeView, CheckCodeView

urlpatterns = [
    path('send_code/', SendCodeView.as_view(), name='send-code'),
    path('check_code/', CheckCodeView.as_view(), name='check-code'),
]
