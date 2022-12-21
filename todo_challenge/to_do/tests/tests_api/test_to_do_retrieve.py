from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from to_do.models import ToDo


class RetrieveToDoTest(APITestCase):
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
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)
        to_do = response.data
        self.assertEqual(to_do['title'], 'titulo1')
        self.assertEqual(to_do['description'], 'descripcion1')
        self.assertEqual(to_do['completed'], False)
        self.assertContains(response, 'created', 1, status_code=200)
        self.assertContains(response, 'last_modification', 1, status_code=200)
        self.assertContains(response, 'id', 1, status_code=200)


class RetrieveWhitoutCredentialsTest(APITestCase):
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
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)
