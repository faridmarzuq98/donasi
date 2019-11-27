from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Campaign(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField()
	goal = models.IntegerField()
	raised = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.title

class UserManager(models.Manager):
	def validator(self, postData):
		errors = {}
		if (postData['first_name'].isalpha()) == False:
			if len(postData['first_name']) < 2:
				errors['first_name'] = "First name can not be shorter than 2 characters"

		if (postData['last_name'].isalpha()) == False:
			if len(postData['last_name']) < 2:
				errors['last_name'] = "Last name can not be shorter than 2 characters"

		if len(postData['email']) == 0:
			errors['email'] = "You must enter an email"

		if len(postData['password']) < 8:
			errors['password'] = "Password is too short!"

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	logged_in = models.BooleanField(default=False)
	phone = models.CharField(max_length=255,default="")
	address = models.TextField(default="")
	objects = UserManager()

# c = Campaign(
# 	title='ini judul ke-4',
# 	description='ini deskripsinya yg ke-4 yang sangat panjaaang panjaaang panjaaang panjaaang panjaaang panjaaang panjaaang panjaaang.',
# 	target_duit_donasi=1050,
# 	total_duit_donasi=300,
# 	total_orang_donasi=15,
# 	pub_date=timezone.now()
# )
