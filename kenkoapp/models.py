from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Carepro(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carepro')
	name = models.CharField(max_length=500)
	number = models.CharField(max_length=500)
	image = models.ImageField(upload_to='carepro_img', blank=False)
	address = models.CharField(max_length=500)

	def __str__(self):
		return self.name

