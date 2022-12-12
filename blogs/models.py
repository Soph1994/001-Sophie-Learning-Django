from django.db import models


# Create your models here.
class Post(models.Model):
	title 		= models.CharField(max_length=255, blank=True, null=True)
	category 	= models.CharField(max_length=255, blank=True, null=True)
	content 	= models.TextField(blank=True, null=True)