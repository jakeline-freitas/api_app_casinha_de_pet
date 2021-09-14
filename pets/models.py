from django.db import models
from uuid import uuid4


def upload_image_pet(instance, filename):
    return f"{instance.id_pet}-{filename}"


class Pet(models.Model):
    id_pet = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=55, blank=False, null=False)
    type = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    vacinne = models.BooleanField()
    owner = models.ForeignKey('accounts.User', verbose_name='Responsável', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_image_pet, blank=True, null=True)

    def __str__(self):
        return self.name