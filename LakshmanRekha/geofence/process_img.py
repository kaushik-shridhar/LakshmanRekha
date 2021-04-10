import cv2
import MySQLdb

def resize_image(image):
    image_name = 'media/'+image
    img = cv2.imread(image_name)
    new_img = cv2.resize(img, (600, 600))
    cv2.imwrite(image_name, new_img)
    return image_name

def image_resize(image, y, first, second):
    image_1 = cv2.imread(image)
    image_new = cv2.resize(image_1, (first, second))
    image_name = './media/'+y
    cv2.imwrite(image_name, image_new)

#print(resize_image('maps/watch1_hoV5XzR.jpg'))

import numpy as np

def image_resize(image, y, first, second):
    image_1 = cv2.imread(image)
    image_new = cv2.resize(image_1, (first, second))
    image_name = './media/'+y
    cv2.imwrite(image_name, image_new)

def image_draw(image, y):
    pts = np.array(c1.x, np.int32)
    pts = pts.reshape((-1,1,2))
    print(c1.x)
    print('POINTS: ',pts)
    isClosed = True
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2
    image_old = cv2.imread(image)
    image_new = cv2.polylines(image_old, [pts], isClosed, color, thickness)
    try:
        mydb = MySQLdb.connect(
            "localhost",
            "root",
            "",
            "lakshmanrekha"
        )
    except:
        print("Can't connect to database")
        return
    mycursor = mydb.cursor()
    print(len(p1.x))
    if len(p1.x) != 0:
        for i in range(len(p1.x)):
            print(p1.x[i])
            image_new = cv2.circle(image_new, (int(p1.x[i]),int(p1.y[i])), radius=3, color=color, thickness=-1)
    else:
        print('len 0 for p1.x executed')
        new_y = y[5:]
        new = new_y.split('.')
        print(new)
        query = "select x, y from tracking_wifi where floor_name = '"+new[0]+"'"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for i in range(len(myresult)):
            image_new = cv2.circle(image_new, (int(float(myresult[i][0])),int(float(myresult[i][1]))), radius=3, color=color, thickness=-1)
    z = y[5:]
    z_1 = 'geofenced_maps/' + z
    image_name = './media/' + z_1
    cv2.imwrite(image_name, image_new)

def image_resize_geo(image, y, first, second):
    z = y[5:]
    z_1 = 'geofenced_maps/' + y
    image_name = './media/' + z_1
    image_1 = cv2.imread(image_name)
    image_new = cv2.resize(image_1, (first, second))
    cv2.imwrite(image_name, image_new)

class coords:
    x = []
    y = []

c1 = coords()

class points:
    x = []
    y = []

p1 = points()

class ssid:
    ssid = []

ssid_obj = ssid()

class mp:
    mp = []

mp_obj = mp()

def appe(start, end):
    c1.x.append(start)
    c1.y.append(end)
    print('x',c1.x ,'y' , c1.y)

def appe_points(x, y):
    p1.x.append(x)
    p1.y.append(y)

def appe_ssid(ssid1, ssid2, ssid3):
    ssid_obj.ssid = [ssid1, ssid2, ssid3]

def appe_mp(mp1, mp2, mp3):
    mp_obj.mp = [mp1, mp2, mp3]
    
def empty_fence():
    c1.x = []
    c1.y = []
    print('c1.x',c1.x ,'c1.y' , c1.y)

def empty_points():
    p1.x = []
    p1.y = []
    print('p1.x', p1.x, 'p1.y', p1.y)