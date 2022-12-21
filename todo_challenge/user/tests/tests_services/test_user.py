
from django.test import TestCase
from user.services.user import UserService


class CreateUserServiceTest(TestCase):

    def test_create(self):
        user = UserService.create('user', 'password')
        self.assertEqual(user.username, 'user')
