from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse    
from .models import Task


def addTask(request):
    t=request.POST['task']
    Task.objects.create(task=t)
    #ompleted_task=Task.objects.filter(is_)
    #return HttpResponse('The form is submitted')
    return redirect ('home')


# Create your views here.
def mark_as_done(request, pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')
    #return HttpResponse(task)

def edit_task(request, pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method =='POST':
        new_task =request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
        #print(new_task)
        
    else:
        context={
            'g':get_task,
        }
        return render (request, 'edit.html',context)
def delete_task(request, pk):
    d_task = get_object_or_404(Task,pk=pk)
    d_task.delete()
    return redirect('home')