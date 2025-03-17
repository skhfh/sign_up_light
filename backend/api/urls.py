from django.urls import path

from .views import sing_up

app_name = 'api'

urlpatterns = [
    path('sing-up/', sing_up),
]
