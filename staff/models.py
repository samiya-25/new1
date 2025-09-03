from django.db import models

# Create your models here.

class Staff(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
