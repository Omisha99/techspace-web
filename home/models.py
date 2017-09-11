from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=255)
	app_name = models.CharField(max_length=255, blank=True)
	email = models.EmailField(max_length=255)
	content = models.TextField()

	def __str__(self):
		return self.name + '-' + self.email + '-' + self.app_name

class Club(models.Model):
	club_name = models.CharField(max_length=255)
	captain = models.CharField(max_length=255, default='null')
	club_image = models.ImageField(upload_to='logo')

	def __str__(self):
		return self.club_name

class Association(models.Model):
	company = models.CharField(max_length=255)
	company_img = models.ImageField(upload_to='associations')

	def __str__(self):
		return self.company

