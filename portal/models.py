from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField


class Person(models.Model):
	first_name   = models.CharField(max_length = 30, blank=True)
	last_name    = models.CharField(max_length =30, blank=True)
	tlf   		 = models.IntegerField(default=11)
	e_post		 = models.CharField(max_length =30)
	
	
	
	def __str__(self):
		return self.first_name



class Publish1(models.Model):

	first_name   = models.CharField(max_length = 30)
	last_name    = models.CharField(max_length =30)
	tlf   		 = models.IntegerField(default=11)
	e_post		 = models.CharField(max_length =30)

	def __str__(self):
		return self.first_name

class Time_Test(models.Model):

	BY_DEL_CHOICES = [
		('fjell', 'Fjell'),
		('sund', 'Sund'),
		('oygarden', 'Øygarden'),
	]
	id = models.AutoField(primary_key=True)
	title        = models.CharField(max_length = 30)
	date_test    = models.DateTimeField()
	bydel		 = MultiSelectField(choices=BY_DEL_CHOICES)
	ham = models.CharField(max_length=30)

	def __str__(self):
		return self.title





class Publish(models.Model):	

	image 		= models.ImageField(upload_to= 'publish_img/')
	title       = models.CharField(max_length = 30)
	description = models.TextField(max_length= 100)
	is_active   = models.BooleanField(default = True)
	created     = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated     = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return self.title
