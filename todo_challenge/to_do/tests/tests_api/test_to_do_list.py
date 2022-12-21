from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class ListToDoTest(APITestCase):
    url = '/api/to_do/'

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def setUp(self):
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)

    def test_list_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        to_do = response.data[0]
        self.assertEqual(to_do['title'], 'titulo1')
        self.assertEqual(to_do['description'], 'descripcion1')
        self.assertEqual(to_do['completed'], False)
        to_do = response.data[1]
        self.assertEqual(to_do['title'], 'titulo2')
        self.assertEqual(to_do['description'], 'descripcion2')
        self.assertEqual(to_do['completed'], True)
        self.assertContains(response, 'created', 2, status_code=200)
        self.assertContains(response, 'last_modification', 2, status_code=200)


class ListWhitoutCredentialsTest(APITestCase):
    url = '/api/to_do/'
    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def test_protect(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
