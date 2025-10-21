from django.shortcuts import render,redirect
from django.http import HttpResponse    
from .models import Task


def addTask(request):
    t=request.POST['task']
    Task.objects.create(task=t)
    #return HttpResponse('The form is submitted')
    return redirect ('home')


# Create your views here.
