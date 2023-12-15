from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, status_choice
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from .form import TaskForm

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})

def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choice': status_choice})
    elif request.method == 'POST':
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            data_of_complited=request.POST.get('data_of_complited'),
            detailed_description=request.POST.get('detailed_description')
        )

        return HttpResponseRedirect('/')


class task_update_view(TemplateView):
    template_name = 'task_update_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(initial={
            'description': task.description,
            'detailed_description': task.detailed_description,
            'data_of_complited': task.data_of_complited,
            'status': task.status,
            'type': task.type
        })
        context['form'] = form
        return context


    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.detailed_description = form.cleaned_data.get('detailed_description')
            task.data_of_complited = form.cleaned_data.get('data_of_complited')
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']

            task.save()
            return redirect('task_update_view', pk=task.pk)
        else:
            return render(request, 'task_update_view.html', {'form': form})


class task_delete_view(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')