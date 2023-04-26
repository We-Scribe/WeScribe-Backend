from django.db import models
from users.models import CustomUser

class Notes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    content = models.TextField()