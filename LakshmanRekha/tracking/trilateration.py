import math
import json
import MySQLdb

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


class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class circle(object):
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

class json_data(object):
    def __init__(self, circles, inner_points, center):
        self.circles = circles
        self.inner_points = inner_points
        self.center = center

def serialize_instance(obj):
    d = {}
    d.update(vars(obj))
    return d

def get_two_points_distance(p1, p2):
    return math.sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2))

def get_two_circles_intersecting_points(c1, c2):
    p1 = c1.center 
    p2 = c2.center
    r1 = c1.radius
    r2 = c2.radius

    d = get_two_points_distance(p1, p2)
    # if to far away, or self contained - can't be done
    if d >= (r1 + r2) or d <= math.fabs(r1 -r2):
        return None

    a = (pow(r1, 2) - pow(r2, 2) + pow(d, 2)) / (2*d)
    h  = math.sqrt(pow(r1, 2) - pow(a, 2))
    x0 = p1.x + a*(p2.x - p1.x)/d 
    y0 = p1.y + a*(p2.y - p1.y)/d
    rx = -(p2.y - p1.y) * (h/d)
    ry = -(p2.x - p1.x) * (h / d)
    return [point(x0+rx, y0-ry), point(x0-rx, y0+ry)]

def get_all_intersecting_points(circles):
    points = []
    num = len(circles)
    for i in range(num):
        j = i + 1
        for k in range(j, num):
            res = get_two_circles_intersecting_points(circles[i], circles[k])
            if res:
                points.extend(res)
    return points

def is_contained_in_circles(point, circles):
    for i in range(len(circles)):
        if (get_two_points_distance(point, circles[i].center) > (circles[i].radius)):
            return False
    return True

def get_polygon_center(points):
    center = point(0, 0)
    num = len(points)
    for i in range(num):
        center.x += points[i].x
        center.y += points[i].y
        
    try:
        center.x /= num
        center.y /= num
    except(ZeroDivisionError):
        print('!!!!!!!!!!!!!value is zero!!!!!!!!!!!')
        pass
    return center

def trilaterate(r1, r2, r3, floor_name):
    r1 = r1*44
    r2 = r2*44
    r3 = r3*44
    # p1 = point(5, 8)
    # p2 = point(9, 4)
    # p3 = point(10, 15)
    print('distance', r1, r2, r3)
    mydb, mycursor = connect_to_db()
    sql = "SELECT x, y FROM tracking_wifi WHERE floor_name='"+floor_name+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall() #(('10', '10), ())
    p1 = point(int(float(result[0][0])), int(float(result[0][1])))
    p2 = point(int(float(result[1][0])), int(float(result[1][1])))
    p3 = point(int(float(result[2][0])), int(float(result[2][1])))

    c1 = circle(p1, r1)
    c2 = circle(p2, r2)
    c3 = circle(p3, r3)

    circle_list = [c1, c2, c3]

    pts = get_all_intersecting_points(circle_list)
    # print(len(pts))

    inner_points = []
    for p in get_all_intersecting_points(circle_list):
        if is_contained_in_circles(p, circle_list):
            inner_points.append(p)

    center = get_polygon_center(inner_points)

    # print(inner_points[0].x)

    # in_json = json_data([c1, c2, c3], [p1, p2, p3], rssi)

    # out_json = json.dumps(in_json, sort_keys=True,
    #                  indent=4, default=serialize_instance)

    # with open("data.json", 'w') as fw:
    #     fw.write(out_json)

    return center

# center = trilaterate(100, 100, 100)
# print(center.x, center.y)