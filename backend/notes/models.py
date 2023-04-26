from django.db import models
from users.models import CustomUser

class Notes(models.Model):
    title = models.CharField(max_length=200, blank=True, default='Notes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    boardID = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)