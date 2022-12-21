from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from to_do.models import ToDo


class DeleteToDoTest(APITestCase):
    url = '/api/to_do/'
    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def setUp(self):
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)

    def _get_url(self, id):
        return self.url + str(id) + '/'

    def test_create_ok(self):
        to_do = ToDo.objects.get(title='titulo1')
        url = self._get_url(to_do.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(ToDo.objects.count(), 3)
        self.assertEqual(ToDo.all_objects.count(), 4)


class DeleteWhitoutCredentialsTest(APITestCase):
    url = '/api/to_do/'
    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def _get_url(self, id):
        return self.url + str(id) + '/'

    def test_protect(self):
        to_do = ToDo.objects.get(title='titulo1')
        url = self._get_url(to_do.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)
