from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_ad = models.DateTimeField('Created', auto_now=True)
	rating = models.IntegerField(default=0)
	author = models.CharField(max_length=255)
	likes = models.ManyToManyField(User)

class Answer(models.Model):
	text = models.TextField()
	added_ad = models.DateTimeField('Created', auto_now=True)
	author = models.CharField(max_length=255)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
