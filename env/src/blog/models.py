from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager 


# Create your models here.

STATUS = (
	(0, "Draft"),
	(1, "Publish"),
	)

class Post(models.Model):
	title = models.TextField()
	author = models.CharField(max_length=100)
	content = models.TextField(max_length=1000,default='')
	slug =  models.SlugField(max_length=120,unique=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	image = models.URLField(null=True)
	search_fields = ['title']
	status = models.IntegerField(choices = STATUS, default=0)
	pub_date = models.DateTimeField(null=True)
	tags = TaggableManager()


	class Meta:
		ordering = ['-created_on']

