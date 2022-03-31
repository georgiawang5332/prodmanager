from django.urls import path
from . import views

app_name = 'miltSear'

urlpatterns = [
  path('', views.milt_sear, name='milt_sear'),
]
