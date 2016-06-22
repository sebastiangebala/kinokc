from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.FileField(null=True, blank=True) 
    display_date = models.DateField(null=True, blank=True)
    godzina = models.TimeField(null=True, blank=True, default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class SignUp(models.Model):
	email = models.EmailField()
	
	def __str__(self):
		return self.email

class Reservation(models.Model):
	imię = models.CharField(max_length=200)
	nazwisko = models.CharField(max_length=200)
	film = models.CharField(max_length=200)
	ilość_biletów = models.CharField(max_length=200)
	dzień = models.DateField(null=True, blank=True)
	godzina = models.TimeField(null=True, blank=True, default=timezone.now)
	

	def __str__(self):
		return self.nazwisko
