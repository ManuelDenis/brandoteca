import requests
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=12, default='')
    message = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super(Message, self).save(*args, **kwargs)
