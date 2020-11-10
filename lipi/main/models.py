from django.db import models

# Create your models here.


class Tal(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        verbose_name="Tal Name",
        unique=True
    )
