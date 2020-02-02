from django.db import models

# Create your models here.
class General(models.Model):
	about = models.TextField(max_length=2000)
	contact = models.TextField(max_length=2000)
	email = models.EmailField()
