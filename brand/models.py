from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(unique=True, default='')

    def __str__(self):
        return str(self.email)

