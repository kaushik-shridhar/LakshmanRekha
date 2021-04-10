from time import time
import MySQLdb
from .alert_system import *
# from .tracking_utils import * !!!do not do this even by mistake
from .trilateration import *
from .conversion import *
import time
import random

def connect_to_db(host='localhost', username='root', password='', db_name='lakshmanrekha'):
    try:
        mydb = MySQLdb.connect(
            host,
            username,
            password,
            db_name
        )
    except:
        print("Can't connect to database")
        return
    mycursor = mydb.cursor()
    return mydb, mycursor

def add():
    print("hello")

def background_check(uid, floor_name):
    mydb, mycursor = connect_to_db()
    sql1 = "SELECT rssi, mp FROM tracking_tracker WHERE uid='"+str(uid)+"'"
    mycursor.execute(sql1)
    result1 = mycursor.fetchall()
    rssi = ''
    mp = ''
    for i in range(len(result1)):
        rssi += result1[i][0]+" "
        mp += result1[i][1]+" "
    mpa = mp.split(" ")
    rssia = rssi.split(" ")
    if rssia[0] != '':
        # print(rssia[0], rssia[1])
        print('background check')
        dist1 = float(convert_rssi(rssia[0], mpa[0]))
        dist2 = float(convert_rssi(rssia[1], mpa[1]))
        # print("dist", dist1, dist2)
        dist3 = float(convert_rssi(rssia[2], mpa[2]))
        center = trilaterate(dist1, dist2, dist3, floor_name)
    # print(rssia)
    # print(mpa)
    # dist1 = float(convert_rssi(rssia[0], mpa[0]))
    # dist2 = float(convert_rssi(rssia[1], mpa[0]))
    # dist3 = float(convert_rssi(rssia[2], mpa[2]))
    # center = trilaterate(dist1, dist2, dist3)
    # print(type(center))
    # print(center.x, center.y)
    # result = inside_test(center.x, center.y, "hall.jpeg")
    # result = inside_test(center.x, center.y, "floor_1.jpeg")
    # if result == 'outside':
    #     notify(uid, floor_name)
    new_array = n1.s.split(" ")
    result = inside_test(float(new_array[0]), float(new_array[1]), "floor_1.jpeg")
    # if result == 'outside':
    #     notify(uid, floor_name)

class new_class:
    s = ''
    old_s = ''
    x = 1
    y = 1
    counter_plus = 0
    counter_minus = 0
    boolean = True
    bool_num = 0

    x_coords = [295, 372, 362, 277, 300, 317, 417, 565, 498, 581, 515, 426, 342]
    y_coords = [400, 455, 344, 307, 220, 112, 31, 92, 174, 335, 367, 377, 379]
    counter = 0

n1 = new_class()


def background_check_live(uid, floor_name):
    mydb, mycursor = connect_to_db()
    sql1 = "SELECT rssi, mp FROM tracking_tracker WHERE uid='"+str(uid)+"' and floor_name = 'floor_1'"
    mycursor.execute(sql1)
    result1 = mycursor.fetchall()
    rssi = ''
    mp = ''
    center = ''
    for i in range(len(result1)):
        rssi += result1[i][0]+" "
        mp += result1[i][1]+" "
    mpa = mp.split(" ")
    rssia = rssi.split(" ")
    # print("rssia", rssia)
    # print("mpa", mpa)
    s = ''
    if rssia[0] != '':
        # print('background check live')
        # print("rssi", rssia[0], rssia[1])
        dist1 = float(convert_rssi(rssia[0], mpa[0]))
        dist2 = float(convert_rssi(rssia[1], mpa[1]))
        dist3 = float(convert_rssi(rssia[2], mpa[2]))
        center = trilaterate(dist1, dist2, dist3, floor_name)
        # print("dist", dist1, dist2, dist3)
        
    # if n1.counter < len(n1.x_coords):
    #     n1.x = n1.x_coords[n1.counter]
    #     n1.y = n1.y_coords[n1.counter]
    #     n1.counter += 1
       
    n1.s = str(n1.x)+" "+str(n1.y)
    new_array = n1.s.split()
    result = inside_test(float(new_array[0]), float(new_array[1]), "floor_1.jpeg")
    # if result == 'outside':
    #     notify('40:F5:20:39:3D:BE', 'floor_1')
    #     notify("40:F5:20:2D:6B:09", "floor_1")
    # print(n1.s)
    # new_array = n1.s.split(" ")
    # result = inside_test(float(new_array[0]), float(new_array[1]), "table.jpeg")
    # if result == 'outside':
    #     notify(uid, floor_name)
    # print(rssia[0], rssia[1])
    # print(mpa[0], mpa[1])
    # dist1 = float(convert_rssi(rssia[0], mpa[0]))
    # dist2 = float(convert_rssi(rssia[1], mpa[0]))
    # dist3 = float(convert_rssi(rssia[2], mpa[2]))
    # center = trilaterate(dist1, dist2, dist3)
    # s = str(center.x)+" "+str(center.y)
    # center = str(200)+" "+str(200)
    print(n1.s)
    return n1.s

# def background_check(ssid, rssi, uid, floor):
#     print("bg check running")
#     mydb, mycursor = connect_to_db()
#     sql1 = "SELECT mp, rssi FROM tracker WHERE uid='"+str(uid)+"'"
#     mycursor.execute(sql1)
#     result1 = mycursor.fetchall()
#     rssi = ''
#     mp = ''
#     for i in range(len(result1)):
#         rssi += result1[i][0] + " "
#         mp += result1[i][1] + " "
#     mpa = mp.split(" ")
#     rssia = rssi.split(" ")
    # dist1 = float(convert_rssi(rssia[0], mpa[0]))
    # dist2 = float(convert_rssi(rssia[1], mpa[0]))
    # dist3 = float(convert_rssi(rssia[2], mpa[2]))
    # center = trilaterate(dist1, dist2, dist3)
#     s = str(200) +" "+str(200)
#     s = str(200) +" "+str(200)
#     pts = s.split(" ")#center.split(" ")
#     pts = center.split(" ")
#     result = inside_test(pts[0], pts[1], "floor_1.jpg")#floor)
#     if (result == 'outside'):
#         notify()

    
# background_check()