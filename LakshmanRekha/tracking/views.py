from django.shortcuts import render
from django.http import HttpResponse
from .alert_system import *
from .background_check import *
from .tracking_utils import *
import time
import datetime
import MySQLdb
from .conversion import *
from .trilateration import *
from django.http import StreamingHttpResponse
from .alert_system import *
from django.contrib import messages

# Create your views here.

# tracking page
class hidden_locn:
    hidden_geofence_locn = ''

locn = hidden_locn()
def index(request):
    if request.method == 'POST':
        hidden_locn.hidden_geofence_locn = ''
        hidden_geofence_locn = request.POST['hidden_geofence_locn']
        hidden_locn.hidden_geofence_locn = hidden_geofence_locn
        print(hidden_geofence_locn)
        # background_check()
        
        return render(request, 'tracking/tracking.html', {'map_image': hidden_geofence_locn})
    # background_check()
    return HttpResponse("Hello world")


def update(request):
    # if request.method == 'POST':
    #     return
        # x = request.POST['x']
        # y = request.POST['y']
        # # print(type(x), '\n')
        # print(x+" "+y)
        # # print(float(x))
        # # print(float(y))
        # print(hidden_locn.hidden_geofence_locn[22:])
        # result = inside_test(float(x), float(y), hidden_locn.hidden_geofence_locn[22:] )
        # # inside_test(float(x), float(y), hidden_locn.hidden_geofence_locn[22:])
        # print(result)
        # # if (result == 'outside'):
        # #     notify()
        # # background_check()
        # return HttpResponse('hello')
    return HttpResponse('hello')

# validate patient
def validate_patient(request):
    if request.method == 'POST':
        # ssid = request.POST['ssid']
        # patient = request.POST['patient']
        # floor_name = request.POST['floor_name']
        # uid = request.POST['uid']
        # check_user(ssid, patient, floor_name, uid)
        uid = request.POST['uid']
        patient_name = request.POST['patient_name']
        floor_name = request.POST['floor_name']
        wifi_ssid = request.POST['wifi_ssid']
        # org = request.POST['org']
        org = 'Hawkeye'
        print(org)
        print(str(request.user.username))
        check_user(uid, patient_name, floor_name, wifi_ssid, str(org))
        # print(uid, patient_name, floor_name, wifi_ssid)
        return HttpResponse('Successfully validated')
    return HttpResponse('get lost')


class new_class:
    ci = ''
    cx = ''
    cy = ''
class old_data:
    cx_past = ''
    cy_past = ''

c1 = new_class()
c2 = old_data()
# user location
def recieve(request):
    if request.method == 'POST':
        a = request.POST['a']
        check_location(a)
        # send = a.split("/")
        
        # c1.ci = send[2]
        # # print(c1.ci)
        # check_location(a)
    return HttpResponse('Successfully tracked')

def sse(request):
    if request.method == 'POST':
        hidden_locn.hidden_geofence_locn = ''
        hidden_geofence_locn = request.POST['hidden_geofence_locn']
        hidden_locn.hidden_geofence_locn = hidden_geofence_locn
        print(hidden_geofence_locn)
        return render(request, 'tracking/index.html', {'map_image': hidden_geofence_locn})
    return HttpResponse("Success")

# ['-44', '-50', '-38', ''] ['-54', '-69', '-41', '']

def stream(request):
    def event_stream():
        while True:
            a = ''
            if request.method == 'POST':
                a = request.POST['a']
                c1.ci = a
                s = check_location_live(a)
            else:
                s = ''
            if s == '':
                messages.warning(request, 'Device not connected')
            # print(c1.ci)
            # print("HE")
            # mydb, mycursor = connect_to_db()
            # sql1 = "SELECT rssi, mp FROM tracker WHERE uid='"+c1.ci+"'"
            # sql1 = "SELECT rssi, mp FROM tracker WHERE uid='40:F5:20:39:3D:BE'"
            # mycursor.execute(sql1)
            # result1 = mycursor.fetchall()
            # rssi = ''
            # mp = ''
            # print(result1)
            # print("EXE")
            # print('old data: ',c2.cx_past, c2.cy_past)
            # for i in range(len(result1)):
            #     rssi += result1[i][0] + " "
            #     mp += result1[i][1] + " "
            # mpa = mp.split(" ")
            # rssia = rssi.split(" ")
            # # mpa = ['-44', '-50', '-38', '']
            # # rssia = ['-54', '-69', '-41', '']
            # print(mpa, rssia)
            # dist1 = float(convert_rssi(rssia[0], mpa[0]))
            # dist2 = float(convert_rssi(rssia[1], mpa[0]))
            # dist3 = float(convert_rssi(rssia[2], mpa[2]))
            # # dist3 = 300
            # center = trilaterate(dist1, dist2, dist3)
            # if center.x == 0 and center.y == 0:
            #     print('retreiving old data')
            #     c1.cx = c2.cx_past
            #     c1.cy = c2.cy_past
            # else:
            #     print('this is the latest data')
            #     c1.cx = center.x
            #     c1.cy = center.y
            #     c2.cx_past = center.x
            #     c2.cy_past = center.y
            # print(c1.ci)
            # # # print(a, "hello w orld whaddup!")
            # print(str(c1.cx) + " " + str(c1.cy))
            time.sleep(3)
            # s = str(200) +" "+str(200)
            # s = str(c1.cx) + " " + str(c1.cy)
            

            # yield 'data: The server time is: %s\n\n' % str(datetime.datetime.now())
            # yield 'data: %s'% str(s) +'\n\n'
            yield 'data: %s' % str(s) +'\n\n'
            # yield 'data: uid: %s\n\n' % str(c1.ci)
            # yield 'data: x coord: %s\n\n' % str(c1.cx)
            # yield 'data: y coord: %s\n\n' % str(c1.cy)
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')