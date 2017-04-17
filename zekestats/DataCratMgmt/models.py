from __future__ import unicode_literals
'''
from django.db import models
from django.contrib.auth.models import User


class Datacrat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.name
'''