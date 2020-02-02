from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField
from django.utils.translation import gettext as _
from django.forms import ModelForm
# Create your models here.
STATUS = (
	(0, "Not Featured"),
	(1, "Featured"),
	)
ACTIVE = (
	(0, "NOT APPROVED"),
	(1, "APPROVED"),
	)


class ShopInfo(models.Model):

	def get_file_path(inst, fn):
		return str(inst.id) + "/" + fn

	id = models.AutoField(primary_key=True, editable=False)
	shop_name = models.CharField(max_length=200,blank=False)
	slug = models.SlugField(max_length=200, unique=True,null=True)
	contact_phone = PhoneField(blank=False,null=True)
	about = models.TextField(max_length=200,blank=False,null=True)
	about2 = models.TextField(max_length=2000,blank=False,null=True)
	address = models.TextField(max_length=75,blank=False,null=True)
	city = models.CharField(max_length=50,blank=False,null=True)
	state = models.CharField(max_length=50,blank=False,null=True)
	country = CountryField(blank=False,null=True)
	zipcode = models.CharField(max_length=20,blank=False,null=True)
	lat = models.FloatField(default=1.0)
	lon = models.FloatField(default=1.0)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	website = models.URLField(max_length=200,blank=True)
	instagram = models.URLField(max_length=200,blank=False)
	images = models.URLField(max_length=400,blank=False,null=True)
	source = models.CharField(max_length=500, blank=False,null=True)
	embed_id = models.CharField(max_length=200,help_text='USE "+" SYMBOLS INSTEAD OF SPACE',null=True)
	status = models.IntegerField(choices = STATUS, default=0)
	active = models.IntegerField(choices = ACTIVE, default=0)
	monday =  models.CharField(max_length=500, blank=False,null=True)
	tuesday =  models.CharField(max_length=500, blank=False,null=True)
	wednesday =  models.CharField(max_length=500, blank=False,null=True)
	thursday =   models.CharField(max_length=500, blank=False,null=True)
	friday = models.CharField(max_length=500, blank=False, null=True)
	saturday =  models.CharField(max_length=500, blank=False,null=True)
	sunday = models.CharField(max_length=500, blank=False,null=True)

	class Meta:
		ordering = ['-shop_name']

	def __unicode__(self):
		return self.shop_name

	def __str__(self):
		return self.shop_name



