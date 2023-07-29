from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from.forms import TodoForm
# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class Tasklist(ListView):
    model=task
    template_name = 'index.html'
    context_object_name = 'obj'

class TaskDetail(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'obj'

class UpdateDetails(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'obj'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class Taskdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
def index(request):
    obj = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        Task=task(name=name,priority=priority,date=date)
        Task.save()
    return render(request,'index.html',{'obj':obj})

def delete(request,taskid):
    if request.method == 'POST':
        Task = task.objects.get(id=taskid)
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    obj=task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=obj)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':obj})