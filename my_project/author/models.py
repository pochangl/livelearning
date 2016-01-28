from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=16)
    birth_time = models.DateTimeField(null=True, default=None)
    birth_date = models.DateField(null=True, default=None)
    age = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, default="")




