from django.shortcuts import render, get_object_or_404
from .models import Task, status_choice
from django.http import HttpResponseRedirect

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'article_view.html', {'task': task})

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html', {'status_choice': status_choice})
    elif request.method == 'POST':
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            data_of_complited=request.POST.get('data_of_complited'),
            detailed_description=request.POST.get('detailed_description')
        )

        return HttpResponseRedirect('/')