from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import MySQLdb

# Create your views here.

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

# home page
def index(request):
    return render(request, 'home/index.html')

# login page
def login_page(request):
    if (request.method == 'POST'):
        user_name = request.POST['org_name']
        pass_word = request.POST['pass']
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request, 'home/login.html')

# registration page
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        org_name = request.POST['org_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(username=org_name).exists():
                return HttpResponse("Username Taken")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already used")
            else:
                user = User.objects.create_user(username=org_name, first_name=first_name, last_name=last_name, email=email, password=pass1)
                user.save()
                return redirect('/login/')
        else:
            return HttpResponse("Passwords do not match")
    else:
        return render(request, 'home/register.html')

# logout page
def logout_page(request):
    logout(request)
    return redirect('/')

# how it works page
def functionality(request):
    return render(request, 'home/functionality.html')

# about page
def about(request):
    return render(request, 'home/about.html')

# contact us page
def contact_us(request):
    return render(request, 'home/contact_us.html')

def return_to_home(request):
    return render(request, 'home/index.html')

def patients(request):
    mydb, mycursor = connect_to_db()
    sql = "SELECT patient_name, floor_name FROM tracking_users WHERE org='"+str(request.user.username)+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    return render(request, 'home/patients.html', {'result': result})