from django.db import models
from django.contrib.auth.models import User
from soft_delete.soft_delete import SoftDeleteModel


class ToDo(SoftDeleteModel):
    title = models.CharField(max_length=50)
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    created = models.DateField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.title

    def set_completed(self) -> None:
        if not self.completed:
            self.completed = True
            self.save()
