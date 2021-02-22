from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import TaskForm
from .models import TaskModel


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            raise ValidationError('Form is not valid.')
    else:
        form = TaskForm()

    all_tasks = TaskModel.objects.all()
    context = {
        'form': TaskForm,
        'all_tasks': all_tasks,
    }
    return render(request, 'accounts/main.html', context)


def task_edit(request, id):
    obj = TaskModel.objects.get(id=id)

    form = TaskForm(instance=obj)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form': form}
    return render(request, 'accounts/task_edit.html', context)


def task_delete(request, id):
    obj = get_object_or_404(TaskModel, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('main')

    context = {'task': obj}
    return render(request, 'accounts/task_delete.html', context)
