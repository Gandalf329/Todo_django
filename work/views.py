from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.
def work_home(request):
    tasks = Task.objects.all()
    return render(request, 'work/work_home.html', {'tasks': tasks})

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'work/create.html'
    form_class = TaskForm

class TaskDetailView(DetailView):
    model = Task
    template_name = 'work/detail.html'
    context_object_name = 'task'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/work'
    template_name = 'work/delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/work')
        else:
            error = 'Form error'

    form = TaskForm()
    data = {
        'form':form,
        'error':error,
        }
    return render(request,'work/create.html',data)
