from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.


class User(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    current_state = models.CharField(max_length=255)


class Step(models.Model):
    state_name = models.CharField(max_length=255)
    response_message = models.TextField()


class Log(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.CharField(max_length=255)
