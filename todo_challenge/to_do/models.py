from django.db import models
from django.utils import timezone
from soft_delete.soft_delete import SoftDeleteModel


class ToDo(SoftDeleteModel):
    title = models.CharField(max_length=50)
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    created = models.DateTimeField(default=timezone.now)
    last_modification = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def set_completed(self) -> None:
        if not self.completed:
            self.completed = True
            self.save()
