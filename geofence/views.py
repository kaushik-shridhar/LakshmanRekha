from django.shortcuts import render

# Create your views here.
def geofence(request):
    return render(request, 'geofence/geofence.html')

def trial(request):
    return render(request, 'geofence/trial.html')