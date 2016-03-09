from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	
	GENDER = (
		('0','Male'),
		('1','Female')
	)

	user = models.ForeignKey(User,on_delete=models.CASCADE)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	gender = models.PositiveSmallIntegerField(choices=GENDER)
	about_me = models.CharField(max_length=1000)
	number_like = models.PositiveSmallIntegerField()
	place = models.CharField(max_length=200)

