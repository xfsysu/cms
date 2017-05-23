from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Union(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=100)
	logo = models.FileField()
	created_time = models.DateTimeField(auto_now=True)
	people = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name


SEX_CHOICES = (
	('M','man'),
	('W','women'),
)

class Member(models.Model):
	union = models.ForeignKey(Union, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	member_id = models.IntegerField(unique=True)
	major = models.CharField(max_length=50)
	sex = models.CharField(max_length=10, choices=SEX_CHOICES)
	add_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.member_id) + '-' + self.name