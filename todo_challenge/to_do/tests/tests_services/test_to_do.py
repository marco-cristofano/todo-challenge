from django.test import TestCase
from django.contrib.auth.models import User
from to_do.services.to_do import ToDoService
from to_do.models import ToDo


class CreateToDoServiceTest(TestCase):

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def test_todo_str(self):
        user = User.objects.get(username='user')
        data = {
            'title': 'titulo',
            'description': 'descripcion',
            'completed': True
        }
        to_do = ToDoService.create(data, user)
        self.assertEqual(to_do.title, 'titulo')
        self.assertEqual(to_do.description, 'descripcion')
        self.assertTrue(to_do.completed)


class CompletedServiceTest(TestCase):

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def test_todo_str(self):
        to_do = ToDo.objects.get(title='titulo1', completed=False)
        ToDoService.completed(to_do)
        self.assertTrue(to_do.completed)
