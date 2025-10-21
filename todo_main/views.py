#from django.http import HttpResponse
from django.shortcuts import render
from TODO.models import Task

def home(request):
    taskABC=Task.objects.filter(is_completed=False).order_by('-updated_at')
    context={
        'tasks1':taskABC
    }
    #print(task)
    return render (request, 'home.html', context)

    #return HttpResponse ('<h1>homepage</h1>')
    