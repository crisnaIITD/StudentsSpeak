from django.db import models
from django.utils import timezone

# Create your models here.
class Speak(models.Model):
    speak_box = models.CharField(max_length=500)
    who_speaks = models.CharField(max_length=25)
    speak_time = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.who_speaks