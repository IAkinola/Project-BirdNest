from django.shortcuts import render

from django_tables2 import SingleTableView
from . import models
from .util import droneInfo, addToDatabase, PilotsTable

class PilotListView(SingleTableView):
    model = models.PilotTable
    table_class = PilotsTable
    template_name = 'drones/index.html'