from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Plugs

import json
import random


# Create your views here.
def index(request):
    data = Plugs.get_average_activity()
    return JsonResponse(data, safe=False)

def avg_by_date(request):
    data = Plugs.get_average_activity_by_date()
    return JsonResponse(data, safe=False)