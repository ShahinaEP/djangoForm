from django.urls import path
from .views import *

urlpatterns = [
    path('banner_list', banner_list, name='banner_list'),
    path('banner_add', banner_add, name='banner_add'),
    path('banner_edit/<pk>', banner_edit, name='banner_edit'),
    path('banner_view/<pk>', banner_view, name='banner_view'),
    path('banner_delete/<pk>', banner_delete, name='banner_delete'),
    # path('contact2', contact2, name='contact2'),
]
