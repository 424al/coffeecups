from django.db import models

# Create your models here.
class Info(models.Model):
	about = models.TextField(max_length=2000)