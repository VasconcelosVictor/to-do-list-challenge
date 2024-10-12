from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tasks, TimeRecord
from datetime import datetime

class TaskViewTests(TestCase):
    
    def setUp(self):
        # Cria um usuário para autenticação
        self.user = User.objects.create_user(username='testuser', password='password')
        self.task = Tasks.objects.create(description="Test Task", user=self.user)

    def test_login_view(self):
        """Caso de teste pra View de Login """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_login_post(self):
        """Caso de teste pra testar a autenticacao"""
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)  # Redireciona após sucesso
        self.assertRedirects(response, reverse('task-list'))

    def test_task_list_view(self):
        """Caso de teste pra testar a listagem de tarefas"""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'task_list.html')

    def test_task_create_view(self):
        """Caso de teste pra testar a Criaçao de uma tarefa"""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('task-add'), {'description': 'New Task'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task-list'))
        self.assertEqual(Tasks.objects.count(), 2)  # Verifica se a nova tarefa foi criada

    def test_task_update_view(self):
        """Caso de teste pra testar Edição de uma tarefa"""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('task-edit', 
                                            kwargs={'pk': self.task.pk}),
                                            {'description': 'Updated Task'})
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.description, 'Updated Task')

    def test_task_delete_view(self):
        """Caso de teste pra testar a Exclusao de uma tarefa"""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('delete_task', kwargs={'task_id': self.task.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tasks.objects.count(), 0)  # Verifica se a tarefa foi deletada

class TimeRecordViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.task = Tasks.objects.create(description="Test Task", user=self.user)

    def test_create_time_record(self):
        """Caso de testes pra testar a criação de um registro de tempo"""
        self.client.login(username='testuser', password='password')
        date_str = datetime.now().strftime('%d/%m/%Y')
        response = self.client.post(reverse('time-add', kwargs={'task_id': self.task.id}), {
            'description': 'Work on project',
            'registration_date': date_str,
            'minutes_worked': '120'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TimeRecord.objects.count(), 1)
        time_record = TimeRecord.objects.first()
        self.assertEqual(time_record.description, 'Work on project')

    def test_delete_time_record(self):
        """Caso de teste pra testar a Exclusao de um registro de tempo"""
        time_record = TimeRecord.objects.create(
            description="Test Time Record", task=self.task, 
            registration_date=datetime.now(), minutes_worked=100
        )
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('delete_record', kwargs={'record_id': time_record.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TimeRecord.objects.count(), 0)  # Verifica se o registro foi deletado

