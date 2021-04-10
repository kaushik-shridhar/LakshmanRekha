from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import MySQLdb
from .process_img import *
import os

# Create your views here.

class boolean:
	test = 0

# geofence home page
def index(request):
	if (request.method=='POST'):
		form = MapForm(request.POST, request.FILES)
		if (form.is_valid()):
			name = form.cleaned_data['name']
			image = form.cleaned_data['upload_locn']
			trial = Map(name=name, upload_locn=image, user=request.user.username, geofence_locn=image, coordinates='0')
			trial.save()
			try:
				db_connection = MySQLdb.connect(
                    "localhost",
                    "root",
                    "",
                    "lakshmanrekha"
                )
			except:
				print("Can't connect to database")
				return
			print("Connected")
			cursor = db_connection.cursor()
			cursor.execute("SELECT upload_locn FROM geofence_map")
			result = cursor.fetchone()
			result = resize_image(result[0])
			return redirect('create_geofence/')
	else:
		form = MapForm()
		return render(request, 'geofence/index.html', {'form': form})

# success page
def success(request):
    return HttpResponse('Successfully Uploaded')

# accessing the maps images
def display_map_images(request):
	if (request.method=='GET'):
        # getting all the objects of Map
		Maps = Map.objects.all()
		return render(request, 'geofence/display_maps.html', {'map_images': Maps})
	return redirect('/geofence/display_maps/')

# creating the geofence
def create_geofence(request):
	if (request.method == 'GET'):
		Maps = Map.objects.last()
		boolean.test = 0
		return render(request, 'geofence/create_geofence.html', {'map_image': Maps.upload_locn.url, 'floor_name': Maps.name})
	if (request.method=='POST'):
		create_geofence.hidden_locn = request.POST['hidden_locn']
		boolean.test = 1
		empty_fence()
		empty_points()
		return render(request, 'geofence/create_geofence.html', {'map_image': create_geofence.hidden_locn})

	return HttpResponse("Yo!")

def delete_geofence(request):
	create_geofence.hidden_locn = request.POST['hidden_locn']
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
	query = "DELETE FROM geofence_map WHERE upload_locn='"+create_geofence.hidden_locn[7:]+"'"
	mycursor.execute(query)
	mydb.commit()
	map_image = '.' + create_geofence.hidden_locn
	geofenced_image = './media/geofenced_maps/' + create_geofence.hidden_locn[11:]
	os.remove(map_image)
	os.remove(geofenced_image)
	return redirect('/geofence/display_maps/')

def my_view_that_sends_coordinates(request):
	x1 = []
	y1 = []
	# if boolean.test == 1:
	# 	empty_fence()
	if request.method == 'POST':
		print('reached post')
		if 'start_x' and 'start_y' in request.POST:
			start_x = request.POST['start_x']
			start_y = request.POST['start_y']
			end_x = request.POST['end_x']
			end_y = request.POST['end_y']
			print(start_x, start_y)
			appe([int(start_x), int(start_y)], [int(end_x), int(end_y)])
			print('success')
			return HttpResponse('Sucess')
		elif 'clearcanva_points' in request.POST:
			empty_points()
			return HttpResponse('Sucess')
		elif 'clearcanva_fence' in request.POST:
			empty_fence()
			return HttpResponse('Sucess')
		else:
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
			ssid = request.POST['ssid']
			mp = request.POST['mp']
			floor_name_1 = request.POST['floor_name']
			print(ssid, mp)
			print(type(ssid))
			print(type(mp))
			mycursor = mydb.cursor()
			query = ''
			if boolean.test == 1:
				
				query = "SELECT upload_locn FROM geofence_map WHERE upload_locn='"+create_geofence.hidden_locn[7:]+"'"
			elif boolean.test == 0:
				query = "SELECT upload_locn FROM geofence_map ORDER BY ID DESC LIMIT 1"
			mycursor.execute(query)
			myresult = mycursor.fetchall()
			x_1 = myresult
			y_1 = x_1[0][0]
			image = './media/'+ y_1
			image_resize(image, y_1, 600, 600)
			image_draw(image, y_1)
			coords_to_be_updated = str(c1.x)
			try:
				mydb_2 = MySQLdb.connect(
					"localhost",
					"root",
					"",
					"lakshmanrekha"
				)
			except:
				print("Can't connect to database")
				return
			mycursor_2 = mydb_2.cursor()
			if boolean.test == 1:
				if ssid != '' and mp != '':
					print('inside ssid')
					ssid_list = ssid.split(', ')
					ssid_obj.ssid = ssid_list
					mp_list = mp.split(', ')
					sql1 = "SELECT * FROM tracking_wifi"
					mycursor_2.execute(sql1)
					result = mycursor_2.fetchall()
					print(ssid_list)
					print(mp_list)
					for i in range(len(ssid_list)):
						flag = 0
						for j in range(len(result)):
							n_ssid = result[j][1]
							if n_ssid == ssid_list[i]:
								flag = 1
							
						if flag == 1:
							print('executing boolean 1 update\n\n')
							if ssid_list[i] != '':
								print(ssid_list[i], 'floor name:',create_geofence.hidden_locn[12:])
								this_floor_name = create_geofence.hidden_locn[12:].split('.')
								sql2 = "UPDATE tracking_wifi SET x='"+str(p1.x[i])+"', y='"+str(p1.y[i])+"' WHERE ssid='"+str(ssid_list[i])+"' AND floor_name='"+this_floor_name[0]+"'"
								mycursor_2.execute(sql2)
								mydb_2.commit()
						else:
							print('executing boolean 1 insert')
							if ssid_list[i] != '':
								this_floor_name = create_geofence.hidden_locn[12:].split('.')
								sql2 = "INSERT INTO tracking_wifi (ssid, mp, floor_name, x, y) VALUES ('"+str(ssid_list[i])+"', '"+str(mp_list[i])+"', '"+this_floor_name[0]+"', '"+str(p1.x[i])+"', '"+str(p1.y[i])+"')"
								mycursor_2.execute(sql2)
								mydb_2.commit()
			elif boolean.test == 0:
				if ssid != '' and mp != '':
					ssid_list = ssid.split(', ')
					mp_list = mp.split(', ')
					sql1 = "SELECT * FROM tracking_wifi"
					mycursor_2.execute(sql1)
					result = mycursor_2.fetchall()
					print(ssid_list)
					print(mp_list)
					for i in range(len(ssid_list)):
						flag = 0
						for j in range(len(result)):
							n_ssid = result[j][1]
							if n_ssid == ssid_list[i]:
								flag = 1
							
						if flag == 1:
							print('executing boolean 0 update\n\n')
							if ssid_list[i] != '':
								sql2 = "UPDATE tracking_wifi SET x='"+str(p1.x[i])+"', y='"+str(p1.y[i])+"' WHERE ssid='"+str(ssid_list[i])+"' AND floor_name='"+floor_name_1+"'"
								mycursor_2.execute(sql2)
								mydb_2.commit()
						else:
							if ssid_list[i] != '':
								print('executing boolean 0 insert')

								sql2 = "INSERT INTO tracking_wifi (ssid, mp, floor_name, x, y) VALUES ('"+str(ssid_list[i])+"', '"+str(mp_list[i])+"', '"+floor_name_1+"', '"+str(p1.x[i])+"', '"+str(p1.y[i])+"')"
								print(sql2)
								mycursor_2.execute(sql2)
								mydb_2.commit()


			query = ''
			if boolean.test == 1:
				mycursor.execute("UPDATE geofence_map SET coordinates = '"+coords_to_be_updated+"' WHERE upload_locn='"+create_geofence.hidden_locn[7:]+"'")
				mydb.commit()
			elif boolean.test == 0:
				mycursor.execute("UPDATE geofence_map SET coordinates = '"+coords_to_be_updated+"' ORDER BY ID DESC LIMIT 1")
				mydb.commit()
			# empty()
			return redirect("/geofence/display_maps/")
	return redirect('/geofence/display_maps/')

def add_ap(request):
	if request.method == 'POST':
		if 'x_coord' and 'y_coord' in request.POST:
			x_coord = request.POST['x_coord']
			y_coord = request.POST['y_coord']
			print('x coordinates:',x_coord,'y coordinates:', y_coord)
			appe_points(float(x_coord), float(y_coord))
			print(p1.x, p1.y)
		
		return HttpResponse("Sucess")
	return HttpResponse("Values inserted")