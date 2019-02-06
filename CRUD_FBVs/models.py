# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Movies(models.Model):


'''''by specifying user as Foreign Key, we're using the builtin User model of django.'''

user = models.ForeignKey(User, on_delete=models.CASCADE)
title = models.CharField(max_length=200)
genre = models.CharField(max_length=200)


def __unicode__(self):
    return self.title


def get_absolute_url(self):
    return reverse('CRUD_FBVs:movies_edit', kwargs={'pk': self.pk})
