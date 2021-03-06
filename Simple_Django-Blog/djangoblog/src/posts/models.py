# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	title = models.CharField(max_length=120)
	author = models.CharField(max_length=120)
	image = models.FileField(null = True, blank = True)
	content = models.TextField()
	update = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	publish = models.DateField(auto_now = False, auto_now_add = False)
	comment = models.ForeignKey('Comment', null = True)

	def __unicode__(self):
		return self.title
		
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs = {"id": self.id})
	
	class Meta:
		ordering = ["-timestamp", "-update"]
		
class Comment(models.Model):
	content = models.TextField(null = True)
	timestamp = models.DateTimeField(null = True)
	author = models.CharField(max_length=120, null = True)

	parent = models.ForeignKey('self', null=True, blank=True)

	def get_children(self):
		return Comment.objects.filter(parent=self)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username


