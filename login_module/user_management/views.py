from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.


def index(request):
    if request.method == 'POST':
        user = request.POST['username']
        pass1 = request.POST['password']

        # Check login with specific user
        if user == "root" and pass1 == "root123":
            return render(request, 'home.html')
    else:
        return render(request, 'index.html')


def ops(request):
    if request.method == 'POST':
        user = request.POST['username']
        blog1 = request.POST['blog']
        url = 'http://localhost:8001/'
        myobj = {'username': user, 'blog':blog1}
        x = requests.post(url, data=myobj)

        return render(request, 'home.html')
    else:
        return render(request, 'index.html')
