from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home
def index(request):
    return render(request, 'login/index.html')

# registration
def register(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        print(first_name)
        return render(request, 'login/index.html')
    else:
        return render(request, 'login/register.html')

# login
def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        return render(request, 'login/index.html')
    else:
        return render(request, 'login/login.html')