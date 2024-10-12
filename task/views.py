from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.views.generic.edit import CreateView ,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .form import *
from .filters import *
from datetime import datetime
from django.core.paginator import Paginator

class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo, {user.username}!")
                return redirect('task-list')
            else:
                messages.error(request, "Usuário ou senha incorretos.")
        else:
            messages.error(request, "Erro ao preencher o formulário.")
        return render(request, 'login.html', {'form': form})
    
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Você foi desconectado com sucesso.")
        return redirect('login')

class TaskListView(LoginRequiredMixin, View):
    def get(self, request, id_record=None):
        tasks = Tasks.objects.filter(user=self.request.user) 
        task_filter = TaskFilter(request.GET, queryset=tasks)
        paginator = Paginator(task_filter.qs, 5)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'task_list.html', {
            'tasks': tasks,
            'filter': task_filter, 
            'page_obj': page_obj })

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = ['description']  
    template_name = 'create_task.html'
    success_url = reverse_lazy('task-list')  

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ['description'] 
    template_name = 'create_task.html'  
    success_url = reverse_lazy('task-list')  

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class DeleteTaskView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Tasks, pk=task_id)
        if task:
            task.delete()
        return redirect('task-list') 
    
class ChangeStatusView(View):
    def get(self,request,task_id):
        task = get_object_or_404(Tasks, pk=task_id)
        if task.status == False:
            task.status = True
        else:
            task.status = False      
        task.save()     
        return redirect('task-list')


class TimeListView(LoginRequiredMixin, View):
    def get(self, request):
        time_record_filter = TimeRecordFilter(request.GET, 
                                              queryset=TimeRecord.objects.all())
        paginator = Paginator(time_record_filter.qs, 5)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'time_list.html', {'page_obj': page_obj,
                                                  'filter': time_record_filter })
    
class CreateTimeRecord(LoginRequiredMixin, View):
    def get(self, request, task_id=None):
        
        time_record = TimeRecord.objects.filter(task=task_id).first() if task_id else None
        task = get_object_or_404(Tasks, pk=task_id) 
        form = TimeRecordForm(instance=time_record)
        return render(request, 'create_time_record.html', {'task':task ,'form': form})

    def post(self, request, task_id=None):
        time_record = TimeRecord.objects.filter(task=task_id).first()
        task = get_object_or_404(Tasks, pk=task_id) 
        form = TimeRecordForm(request.POST, instance=time_record)
        if form.is_valid():
            if time_record == None:
                time_record = TimeRecord()

            time_record.user = request.user  
            date = datetime.strptime(request.POST.get('registration_date'), '%d/%m/%Y')
            time_record.registration_date = date
            time_record.description = request.POST.get('description')
            time_record.minutes_worked = int(request.POST.get('minutes_worked'))
            time_record.task = task
            time_record.save()
            return redirect('task-list') 
        
        else:
            print(form.errors)
        tasks = Tasks.objects.filter(user=self.request.user)
        return render(request, 'create_time_record.html', {'task': task, 'form': form})
    

class DeleteRecordView(View):
    def get(self, request, record_id):
        record = get_object_or_404(TimeRecord, pk=record_id)
        if record:
            record.delete()
        return redirect('task-list')     
        
    

   


