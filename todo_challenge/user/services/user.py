from django.contrib.auth.models import User


class UserService:

    @staticmethod
    def create(username: str, password: str) -> User:
        user = User.objects.create_user(
            username=username,
            password=password
        )
        return user
