import MySQLdb
from .background_check import add, background_check, background_check_live

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

def check_user(uid, patient_name, floor_name, wifi_ssid, org_name):
    mydb, mycursor = connect_to_db()
    sql1 = "SELECT * FROM tracking_users"
    mycursor.execute(sql1)
    result1 = mycursor.fetchall()
    flag = 0
    for i in range(len(result1)):
        n_uid = result1[i][1]
        n_patient_name = result1[i][2]
        n_floor_name = result1[i][3]
        n_wifi_ssid = result1[i][4]
        
        if n_uid==uid and n_patient_name==patient_name and n_floor_name==floor_name and n_wifi_ssid==wifi_ssid:
            flag = 1
        else:
            flag = 0
    if flag == 0:
        sql2 = "INSERT INTO tracking_users (uid, patient_name, floor_name, wifi_ssid, org) VALUES ('"+str(uid)+"', '"+str(patient_name)+"', '"+str(floor_name)+"', '"+str(wifi_ssid)+"','"+org_name+"')"
        mycursor.execute(sql2)
        mydb.commit()

# def check_user(uid, patient_name, floor_name, ssid):
#     mydb, mycursor = connect_to_db(db_name='final')
#     sql1 = "SELECT * FROM users"
#     mycursor.execute(sql1)
#     result = mycursor.fetchall()
#     flag = 0
#     for i in range(len(result)):
#         n_name = result[i][0]
#         n_uid = result[i][1]
#         n_floor = result[i][2]
#         n_ssid = result[i][3]
#         if (n_name == patient and n_uid == uid and n_floor == floor_name and n_ssid == ssid):
#             flag = 1
#         else:
#             flag = 0
#     if flag == 0:
#         sql2 = "INSERT INTO users (uid, patient_name, floor_name, ssid) VALUES ('"+str(floor_name)+"', '"+str(patient_name)+"', '"+str(floor_name)+"', '"+str(ssid)+"')"
#         mycursor.execute(sql2)
#         mydb.commit()
#         # print("flag is 0")
#     else:
#         print("flag is 1")

def check_location(a):
    mydb, mycursor = connect_to_db()
    arr = a.split(",")
    uid = ''
    floor_name = ''
    for a in arr:
        try:
            flag = 0
            y = a.split("/")
            ssid = y[0]
            rssi = y[1]
            uid = y[2]
            floor_name = y[3]
            sql1 = "SELECT * FROM tracking_tracker"
            mycursor.execute(sql1)
            result1 = mycursor.fetchall()
            # print(ssid, rssi, uid, floor_name)
            for i in range(len(result1)):
                n_uid = result1[i][0]
                n_ssid = result1[i][1]
                n_rssi = result1[i][2]
                n_floor_name = result1[i][3]
                n_mp = result1[i][4]
                # print("n", n_ssid, n_floor_name, n_uid)
                
                if n_ssid==ssid and n_floor_name==floor_name and n_uid==uid:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 1:
                sql2 = "UPDATE tracking_tracker SET rssi='"+str(rssi)+"' WHERE ssid='"+str(ssid)+"' AND floor_name='"+str(floor_name)+"' AND uid='"+str(uid)+"'"
                mycursor.execute(sql2)
                mydb.commit()
            else:
                sql2 = "SELECT mp FROM tracking_wifi WHERE ssid='"+str(ssid)+"'"
                mycursor.execute(sql2)
                result2 = mycursor.fetchone()

                sql3 = "INSERT INTO tracking_tracker (uid, ssid, rssi, floor_name, mp) VALUES ('"+str(uid)+"', '"+str(ssid)+"', '"+str(rssi)+"', '"+str(floor_name)+"', '"+str(result2[0])+"')"
                mycursor.execute(sql3)
                mydb.commit()
            # print(ssid, rssi, uid, floor_name)
        except:
            pass
    background_check(uid, floor_name)
    # print(a)

def check_location_live(a):
    mydb, mycursor = connect_to_db()
    arr = a.split(",")
    uid = ''
    floor_name = ''
    for a in arr:
        try:
            flag = 0
            y = a.split("/")
            ssid = y[0]
            rssi = y[1]
            uid = y[2]
            floor_name = y[3]
            sql1 = "SELECT * FROM tracking_tracker"
            mycursor.execute(sql1)
            result1 = mycursor.fetchall()
            for i in range(len(result1)):
                n_uid = result1[i][0]
                n_ssid = result1[i][1]
                n_rssi = result1[i][2]
                n_floor_name = result1[i][3]
                n_mp = result1[i][4]

                if n_ssid==ssid and n_floor_name==floor_name and n_uid==uid:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 1:
                sql2 = "UPDATE tracking_tracker SET rssi='"+str(rssi)+"' WHERE ssid='"+str(ssid)+"' AND floor_name='"+str(floor_name)+"' AND uid='"+str(uid)+"'"
                mycursor.execute(sql2)
                mydb.commit()
                print("update rssi statemetnt")
            else:
                sql2 = "SELECT mp FROM tracking_wifi WHERE ssid='"+str(ssid)+"'"
                mycursor.execute(sql2)
                result2 = mycursor.fetchone()

                sql3 = "INSERT INTO tracking_tracker (uid, ssid, rssi, floor_name, mp) VALUES ('"+str(uid)+"', '"+str(ssid)+"', '"+str(rssi)+"', '"+str(floor_name)+"', '"+str(result2[0])+"')"
                mycursor.execute(sql3)
                mydb.commit()
                print("insertion statement")
            # print(ssid, rssi, uid, floor_name)
        except:
            pass
    center = background_check_live(uid, floor_name)
    return center
    

# def check_location(a):
#     print('working')
#     mydb, mycursor = connect_to_db()
#     flag = 0
#     # print(a)
#     arr = a.split(",")
#     # print(arr)
#     for a in arr:
#         try:
#             y = a.split("/")
#             # print(y)
#             ssid = y[0]
#             # print('ssid: ',ssid,'\n')
#             rssi = y[1]
#             # print('rssi',rssi)
#             uid = y[2]
#             # print('uid',uid)
#             floor = y[3]
#             # print('floor',floor)

#             sql1 = "SELECT * FROM tracker"
#             mycursor.execute(sql1)
#             result1 = mycursor.fetchall()
#             # print(result1)
#             for i in range(len(result1)):
#                 n_ssid = result1[i][1]
#                 # print("for loop working")
#                 # print(i,'n_ssid',n_ssid)
#                 n_floor = result1[i][3]
#                 n_uid = result1[i][0]

#                 if (n_ssid == ssid and n_floor == floor and n_uid == uid):
#                     # print(1, n_ssid, True)
#                     # print("1st if working")
#                     flag = 1
#                     break
                    
#             if flag == 1:
#                 # print('check',n_ssid)
#                 sql2 = "update tracker set rssi='"+str(rssi)+"' where ssid='"+str(n_ssid)+"' and uid='"+str(n_uid)+"' and floor_name='"+str(n_floor)+"'"
#                 mycursor.execute(sql2)
#                 # print("2nd if working")
#                 # print(n_ssid,'executed')
#                 mydb.commit()
                
#             else:
#                 # print(ssid)
#                 sql3 = "SELECT mp FROM wifi WHERE ssid='"+str(ssid)+"'"
#                 # print(sql3)
#                 mycursor.execute(sql3)
#                 # print("3rd if working")
#                 result2 = mycursor.fetchone()
#                 # print(result2)
#                 # print(result2)
                
#                 sql2 = "INSERT INTO tracker (uid, ssid, rssi, floor_name, mp) VALUES ('"+str(uid)+"', '"+str(ssid)+"', '"+str(rssi)+"', '"+str(floor)+"', '"+str(result2[0])+"')"
#                 mycursor.execute(sql2)
#                 mydb.commit()
#                 # print("3rd if working")
#             print(ssid)
#             print(rssi)
#             print(uid)
#             print(floor)
            
#             background_check(ssid, rssi, uid, floor)
#         except:
#             pass
#             # print('vataaaa')
            
            
    

# check_location("hello;hello;hello;hello,")