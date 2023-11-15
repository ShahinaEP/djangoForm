from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home2', home, name='home2'),
]
