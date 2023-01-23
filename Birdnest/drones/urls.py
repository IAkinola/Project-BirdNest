from django.urls import path
from . import views
from drones.views import pilotList

urlpatterns = [
    path("", views.pilotList)
]
