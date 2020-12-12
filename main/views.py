from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# index page
def index(request):
    return render(request, 'main/index.html')

# registration page
def registration(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        return HttpResponse(first_name)
    else:
        return render(request, 'main/register.html')   

# login page
def login(request):
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        return HttpResponse(email)
    else:
        return render(request, 'main/login.html')

# 'how it works' page
def functionality(request):
    return render(request, 'main/functionality.html')