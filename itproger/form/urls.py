from django.urls import path
from . import  views


urlpatterns = [
    path('', views.form_home, name='form_home'),
]