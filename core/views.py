from django.shortcuts import render
from django.conf import settings

def map(request):
    return render(request, 'core/map.html', {'MAPBOX_TOKEN': settings.MAPBOX_TOKEN})
