from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

class Tuple(models.Model):
	parent = models.CharField(max_length=100)
	child = models.CharField(max_length=100)
	pos = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	neg = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	sump = models.IntegerField(default=0,validators=[MinValueValidator(0)])

	def __str__(self):
		return f'{self.parent}-{self.child}'

class UserPairs(models.Model):
	verifyNumber = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pairs")
	tuples = models.ManyToManyField(Tuple, null=True, blank=True)

	def __str__(self):
		return f'{self.user.username}'