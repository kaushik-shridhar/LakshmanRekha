from django.shortcuts import render

# Create your views here.
def geofence(request):
    return render(request, 'geofence/geofence.html')