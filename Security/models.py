from django.db import models

# Create your models here.
class user_entries(models.Model):
	Name = models.CharField(max_length=70)	
	Entry_time = models.TimeField(auto_now_add=False, auto_now=False)
	Reason_of_visit = models.CharField(max_length=250) 
	Whom_to_meet = models.CharField(max_length=250)
	Exit_time = models.TimeField(auto_now_add=False, auto_now=False)
	def __str__(self):
		return self.Name