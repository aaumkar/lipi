from django.urls import path

from . views import *

urlpatterns = [
    path('', show, name="index"),
    path('teental/', teental, name='teental'),
]
