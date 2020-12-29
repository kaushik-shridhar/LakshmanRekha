from django.shortcuts import render
from json import dumps
from tracking.trilateration import *
import datetime
import time
from django.http import StreamingHttpResponse
from tracking.convert import *

def stream(request):
    def event_stream():
        while True:
            time.sleep(3)
            yield 'data: The server time is: %s\n\n' % datetime.datetime.now()
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

# Create your views here.

# index
def index(request):
    if (request.method == 'POST'):
        ssid = request.POST['ssid']
        rssi = request.POST['rssi']
        # print(ssid)
        # print(rssi)
        # center = trilaterate(100, 100, 100, rssi)
        # dataDictionary = {
        #     'x': center.x,
        #     'y': center.y
        # }
        # dataJson = dumps(dataDictionary)
        # return render(request, 'tracking/index.html', {'data': dataJson})
        # distance = convert_rssi(-35, int(rssi), 2)
        distance = convert_rssi2(rssi)
        print(distance)
    # dataDictionary = {
    #     'x': 400,
    #     'y': 400
    # }
    # dataJson = dumps(dataDictionary)
        #return render(request, 'tracking/index.html', {'data':dataJson})
    return render(request, 'tracking/index.html') #{'data':dataJson})