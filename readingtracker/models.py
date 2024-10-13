from django.db import models
from django.conf import settings

class ReadingSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    reading_time = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"
