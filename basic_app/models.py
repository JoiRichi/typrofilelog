from django.db import models
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
	name =  models.CharField(max_length=123, null=True)
	location = models.CharField(max_length=123, null=True)
	age = models.PositiveIntegerField()
	text_field = models.TextField()

	def get_absolute_url(self):
		return reverse ('basic_app:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name

	