from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# index page
def index(request):
    return render(request, 'main/index.html')

# registration page
def register(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        org_name = request.POST['org_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if (pass1 == pass2):
            if (User.objects.filter(username=org_name).exists()):
                return HttpResponse("Username Taken")
            elif (User.objects.filter(email=email).exists()):
                return HttpResponse("Email already used")
            else:
                user = User.objects.create_user(username=org_name, first_name=first_name, last_name=last_name, email=email, password=pass1)
                user.save()
                return redirect('/')
        else:
            return HttpResponse("Passwords do not match")
    else:
        return render(request, 'main/register.html')  

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
        return render(request, 'main/login.html')

# logout view
def logout_page(request):
    logout(request)
    return redirect('/')

# 'how it works' page
def functionality(request):
    return render(request, 'main/functionality.html')