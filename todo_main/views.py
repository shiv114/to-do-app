#from django.http import HttpResponse
from django.shortcuts import render
from TODO.models import Task

def home(request):
    taskABC=Task.objects.filter(is_completed=False).order_by('-updated_at')
    task_completed=Task.objects.filter(is_completed=True)
    context={
        'tasks1':taskABC,
        'task_completed':task_completed,
    }
    #print(task)
    return render (request, 'home.html', context)

    #return HttpResponse ('<h1>homepage</h1>')
    