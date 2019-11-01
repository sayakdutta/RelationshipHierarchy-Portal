from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Tuple(models.Model):
	parent = models.CharField(max_length=100)
	child = models.CharField(max_length=100)
	pos = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	neg = models.IntegerField(default=0,validators=[MinValueValidator(0)])

	def __str__(self):
		return f'{self.parent}-{self.child}'