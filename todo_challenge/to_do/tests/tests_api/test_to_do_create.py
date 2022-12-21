from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class CreateToDoTest(APITestCase):
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

    def test_create_ok(self):
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data), 6)
        to_do = response.data
        self.assertEqual(to_do['title'], 'titulo')
        self.assertEqual(to_do['description'], 'descripcion')
        self.assertTrue(to_do['completed'])
        self.assertContains(response, 'id', 1, status_code=201)
        self.assertContains(response, 'created', 1, status_code=201)
        self.assertContains(response, 'last_modification', 1, status_code=201)

    def test_create_only_title(self):
        body = {'title': 'titulo'}
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data), 6)
        to_do = response.data
        self.assertEqual(to_do['title'], 'titulo')
        self.assertEqual(to_do['description'], None)
        self.assertEqual(to_do['completed'], False)
        self.assertContains(response, 'id', 1, status_code=201)
        self.assertContains(response, 'created', 1, status_code=201)
        self.assertContains(response, 'last_modification', 1, status_code=201)


class CreateToDoErrorTest(APITestCase):
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

    def test_create_empty(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, 'title', 1, status_code=400)
        self.assertContains(response, 'required', 1, status_code=400)

    def test_create_without_title(self):
        body = self.body.copy()
        body.pop('title')
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, 'title', 1, status_code=400)
        self.assertContains(response, 'required', 1, status_code=400)


class CreateWhitoutCredentialsTest(APITestCase):
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

    def test_protect(self):
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, 401)
