from datetime import datetime
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from to_do.models import ToDo


class UpdateToDoTest(APITestCase):
    url = '/api/to_do/'
    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )
    body = {
        'title': 'titulo',
        'description': 'descripcion',
        'completed': True
    }

    def setUp(self):
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        self.to_do = ToDo.objects.create(
            title='titulo1',
            description='descripcion1',
            completed=False,
            user=user
        )

    def _get_url(self, id):
        return self.url + str(id) + '/'

    def test_update_ok(self):
        url = self._get_url(self.to_do.id)
        response = self.client.put(url, self.body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 6)
        to_do = response.data
        self.assertEqual(to_do['title'], 'titulo')
        self.assertEqual(to_do['description'], 'descripcion')
        self.assertTrue(to_do['completed'])
        self.assertContains(response, 'created', 1, status_code=200)
        self.assertContains(response, 'id', 1, status_code=200)
        self.assertContains(response, 'last_modification', 1, status_code=200)
        last_modification = datetime.fromisoformat(to_do['last_modification'])
        self.assertTrue(self.to_do.last_modification < last_modification)

    def test_only_title(self):
        body = {'title': 'titulo'}
        url = self._get_url(self.to_do.id)
        response = self.client.put(url, body)
        self.assertEqual(len(response.data), 6)
        to_do = response.data
        self.assertEqual(to_do['title'], 'titulo')
        self.assertEqual(to_do['description'], 'descripcion1')
        self.assertFalse(to_do['completed'])
        self.assertContains(response, 'created', 1, status_code=200)
        self.assertContains(response, 'last_modification', 1, status_code=200)
        self.assertContains(response, 'id', 1, status_code=200)
        last_modification = datetime.fromisoformat(to_do['last_modification'])
        self.assertTrue(self.to_do.last_modification < last_modification)


class UpdateToDoErrorTest(APITestCase):
    url = '/api/to_do/'
    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )
    body = {
        'title': 'titulo',
        'description': 'descripcion',
        'completed': True

    }

    def setUp(self):
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        self.to_do = ToDo.objects.create(
            title='titulo1',
            description='descripcion1',
            completed=False,
            user=user
        )

    def _get_url(self, id):
        return self.url + str(id) + '/'

    def test_empty(self):
        url = self._get_url(self.to_do.id)
        response = self.client.put(url, {})
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, 'title', 1, status_code=400)
        self.assertContains(response, 'required', 1, status_code=400)

    def test_only_description(self):
        body = {'description': 'description'}
        url = self._get_url(self.to_do.id)
        response = self.client.put(url, body)
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, 'title', 1, status_code=400)
        self.assertContains(response, 'required', 1, status_code=400)

    def test_only_completed(self):
        body = {'completed': True}
        url = self._get_url(self.to_do.id)
        response = self.client.put(url, body)
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, 'title', 1, status_code=400)
        self.assertContains(response, 'required', 1, status_code=400)


class UpdateWhitoutCredentialsTest(APITestCase):
    url = '/api/to_do/'
    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )
    body = {
        'title': 'titulo',
        'description': 'descripcion',
        'completed': True
    }

    def setUp(self):
        user = User.objects.get(username='user')
        self.to_do = ToDo.objects.create(
            title='titulo1',
            description='descripcion1',
            completed=False,
            user=user
        )

    def _get_url(self, id):
        return self.url + str(id) + '/'

    def test_protect(self):
        url = self._get_url(self.to_do.id)
        response = self.client.put(url, self.body)
        self.assertEqual(response.status_code, 401)
