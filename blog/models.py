from django.db import models


class Post(models.Model):
	name = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name} {self.genre}"