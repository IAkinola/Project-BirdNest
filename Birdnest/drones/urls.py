from django.urls import path
from . import views
from drones.views import PilotListView

urlpatterns = [
    path("drones/", PilotListView.as_view())
]
