from django.shortcuts import render

from django_tables2 import SingleTableView
from . import models
from . import util


def pilotList(request):
    table = util.PilotsTable(models.PilotTable.objects.all())

    return render(request, "drones/index.html", {
        "table": table
    })