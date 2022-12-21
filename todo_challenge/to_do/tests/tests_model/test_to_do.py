from django.test import TestCase
from to_do.models import ToDo


class StrTest(TestCase):

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def test_todo_str(self):
        to_do = ToDo.objects.get(title='titulo1')
        self.assertEqual(to_do.__str__(), 'titulo1')


class SetCompletedTest(TestCase):

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def test_todo_str(self):
        to_do = ToDo.objects.get(
            title='titulo1',
            completed=False
        )
        to_do.set_completed()
        self.assertTrue(to_do.completed)
