from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('config.api_v1')),
    path('docs/', include('config.docs')),
]
