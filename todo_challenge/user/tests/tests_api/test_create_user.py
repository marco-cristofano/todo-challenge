from rest_framework.test import APITestCase


class CreateUserTest(APITestCase):
    url = '/user/'
    fixtures = (
        'user/fixtures/user.json',
        'to_do/fixtures/to_do.json',
    )
    body = {
        'username': 'user3',
        'password': 'user3',
    }

    def test_create_ok(self):
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data), 2)
        user = response.data
        self.assertEqual(user['username'], 'user3')
        self.assertContains(response, 'id', 1, status_code=201)

    def test_create_usernamne_repeat(self):
        body = self.body.copy()
        body['username'] = 'user'
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, 400)
        self.assertContains(
            response, 'username already exists', 1, status_code=400)
