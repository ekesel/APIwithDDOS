from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class uploaded(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    files = models.FileField(upload_to='files/%Y/%m/%d')