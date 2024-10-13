from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_item')  # Link item to a user
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.description} at {self.time}'
