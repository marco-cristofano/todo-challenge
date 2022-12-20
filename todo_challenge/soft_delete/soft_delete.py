from django.db import models


class SoftDeleteModelManager(models.Manager):
    '''
    Model Manager para clases con borrado logico
    '''

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class SoftDeleteModel(models.Model):
    '''
    Clase que implementa el borrado logico de instancias en el sistema.
    - Agrega el campo bool deleted
    - Sustituye el model manager por uno que considera el campo deleted
    '''
    deleted = models.BooleanField(default=False)
    objects = SoftDeleteModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()
