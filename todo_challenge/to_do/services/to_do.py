from typing import Dict
from django.contrib.auth.models import User
from to_do.models import ToDo


class ToDoService:

    @staticmethod
    def create(data: Dict, user: User) -> ToDo:
        data['user'] = user
        to_do = ToDo.objects.create(**data)
        return to_do

    @staticmethod
    def completed(to_do: ToDo) -> ToDo:
        to_do.set_completed()
        return to_do
