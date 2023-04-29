from django.db import models
from users.models import CustomUser

class Notes(models.Model):
    title = models.CharField(max_length=200, blank=True, default='Notes')
    description = models.TextField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    boardID = models.CharField(max_length=200, blank=True)
    videoLink = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)