from django.test import TestCase
from to_do.models import ToDo


class StrTest(TestCase):

    def test_todo_str(self):
        to_do = ToDo.objects.create(
            title='titulo',
            description='descripcion'
        )
        self.assertEqual(to_do.__str__(), 'titulo')


class SetCompletedTest(TestCase):

    def test_todo_str(self):
        to_do = ToDo.objects.create(
            title='titulo',
            description='descripcion',
            completed=False
        )
        to_do.set_completed()
        self.assertTrue(to_do.completed)
