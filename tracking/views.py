from django.shortcuts import render

# Create your views here.

# index
def index(request):
    if (request.method == 'POST'):
        ssid = request.POST['ssid']
        rssi = request.POST['rssi']
        print(ssid)
        print(rssi)
    return render(request, 'tracking/index.html')