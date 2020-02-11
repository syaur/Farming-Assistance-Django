from django.db import models
from profiles.models import User

# Create your models here.


intrested_our_blog = (
			('Instant','Instant'),
			('Daily','Daily'),
			('Weekly','Weekly'),
			('Monthly','	Monthly'),
	)


class Contactus(models.Model):

	fname = models.CharField(max_length = 20)

	lname = models.CharField(max_length = 20)

	comment = models.CharField(max_length = 200)

	our_blog = models.CharField(max_length = 9, choices = intrested_our_blog)

	email_id = models.EmailField()

	phone = models.IntegerField()

	about = models.CharField(max_length = 100, null = True, blank = True)

	

