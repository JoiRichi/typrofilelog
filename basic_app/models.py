from django.db import models

# Create your models here.

class Name(models.Model):
	name = models.CharField(max_length=123, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Profile(models.Model):
	name =  models.ForeignKey(Name, null=True, on_delete=models.CASCADE, related_name='identity')
	location = models.CharField(max_length=123, null=True)
	age = models.PositiveIntegerField()
	text_field = models.TextField()

	def __str__(self):
		return self.name.name