from django.db import models

import datetime
from django.utils import timezone

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

# c = Campaign(
# 	title='ini judul ke-4',
# 	description='ini deskripsinya yg ke-4 yang sangat panjaaang panjaaang panjaaang panjaaang panjaaang panjaaang panjaaang panjaaang.',
# 	target_duit_donasi=1050,
# 	total_duit_donasi=300,
# 	total_orang_donasi=15,
# 	pub_date=timezone.now()
# )
