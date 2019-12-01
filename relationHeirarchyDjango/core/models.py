from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Tuple(models.Model):
	parent = models.CharField(max_length=100)
	child = models.CharField(max_length=100)
	pos = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	neg = models.IntegerField(default=0,validators=[MinValueValidator(0)])

	def __str__(self):
		return f'{self.parent}-{self.child}'


# class TupleCopy(models.Model):
# 	id = models.IntegerField(validators=[MinValueValidator(0)], primary_key=True)
# 	parent = models.CharField(max_length=100)
# 	child = models.CharField(max_length=100)
# 	sump = models.IntegerField(default=0,validators=[MinValueValidator(0)])
# 	# neg = models.IntegerField(default=0,validators=[MinValueValidator(0)])

# 	def __str__(self):
# 		return f'{self.parent}-{self.child}'	

# class RangeIndex(models.Model):
# 	startIndex = models.IntegerField(default=0,validators=[MinValueValidator(0)])
# 	# endIndex = models.IntegerField(default=0, validators=[MinValueValidator(0)])