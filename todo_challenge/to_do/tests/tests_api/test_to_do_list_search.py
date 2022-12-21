from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class SearchTitleListToDoTest(APITestCase):
    url = '/api/to_do/?'

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def setUp(self):
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)

    def test_list_user_titulo1(self):
        url = self.url + 'title=titulo1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        to_do = response.data[0]
        self.assertEqual(to_do['title'], 'titulo1')
        self.assertEqual(to_do['description'], 'descripcion1')
        self.assertEqual(to_do['completed'], False)

    def test_list_user_titulo3(self):
        url = self.url + 'title=titulo3'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_list_user_titulo_a(self):
        # titulo_a belongs to another user
        url = self.url + 'title=titulo_a'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)


class SearchCreatedListToDoTest(APITestCase):
    url = '/api/to_do/?'

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def setUp(self):
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)

    def test_list_user_created_ok(self):
        url = self.url + 'created=2022-12-19'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        to_do = response.data[0]
        self.assertEqual(to_do['title'], 'titulo1')
        self.assertEqual(to_do['description'], 'descripcion1')
        self.assertEqual(to_do['completed'], False)

    def test_list_user_created_bad(self):
        url = self.url + 'created=2022-12-21'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)


class SearchCreatedTitleListToDoTest(APITestCase):
    url = '/api/to_do/?'

    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )

    def setUp(self):
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)

    def test_list_user_ok(self):
        url = self.url + 'title=titulo1&created=2022-12-19'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        to_do = response.data[0]
        self.assertEqual(to_do['title'], 'titulo1')
        self.assertEqual(to_do['description'], 'descripcion1')
        self.assertEqual(to_do['completed'], False)

    def test_list_user_bad(self):
        url = self.url + 'title=titulo2&created=2022-12-19'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
