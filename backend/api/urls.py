from django.urls import path

from .views import sign_up

app_name = 'api'

urlpatterns = [
    path('sign-up/', sign_up),
]
