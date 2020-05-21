from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from bug_project import settings


# Create your models here.

STATUS_CHOICES = (('new', 'New'),
                  ('in_progress', 'In Progress'),
                  ('done', 'Done'),
                  ('invalid', 'Invalid'))


class Author(AbstractUser):
    pass


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    time = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    status = models.CharField(max_length=128, choices=STATUS_CHOICES)
    # From https://stackoverflow.com/questions/29691116/django-1-7-add-or-change-a-related-name-argument-to-the-definition-for
    user_filed = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='filed')
    user_assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned', null=True, blank=True)
    user_completed = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='completed', null=True, blank=True)
