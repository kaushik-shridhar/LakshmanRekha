from shapely.geometry import Point, Polygon
import MySQLdb
from plyer import notification
from playsound import playsound

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

def inside_test(point_x, point_y, floor_name):
    try:
        db_connection = MySQLdb.connect(
            "localhost",
            "root",
            "",
            "lakshmanrekha"
        )
    except:
        print("Can't connect to database")

    # print("Connected")
    print(floor_name)

    cursor = db_connection.cursor()
    floor = floor_name.split(".")
    
    print(floor[0])
    cursor.execute("SELECT coordinates FROM geofence_map WHERE name='" + floor[0] + "'")
    result = cursor.fetchone()
    print(result)
    x = result[0]
    final_result = []
    temp = ''
    temp_coords = []

    y = x.split('],')
    for i in y:
        for j in i:
            if j.isdigit():
                temp += j
            if j == ',':
                temp = int(temp)
                temp_coords.append(temp)
                temp = ''
        temp = int(temp)
        temp_coords.append(temp)
        temp = ''
        temp_coords = tuple(temp_coords)
        final_result.append(temp_coords)
        temp_coords = []

    # print(final_result)
    poly = Polygon(final_result)

    x = Point(point_x, point_y)

    if x.within(poly):
        return 'inside'
    else:
        return 'outside'

def notify(uid, floor_name):
    mydb, mycursor = connect_to_db()
    sql = "SELECT patient_name FROM tracking_users WHERE uid='"+str(uid)+"'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    notification.notify(
        title = 'breach alert',
        message = 'patient '+str(result[0])+' has breached the geofence at floor '+str(floor_name),
        timeout = 1
    )
    # playsound('beep.mp3')

# notify("40:F5:20:2D:6B:09", "hall")

# new = inside_test(100, 250)
# print(new)