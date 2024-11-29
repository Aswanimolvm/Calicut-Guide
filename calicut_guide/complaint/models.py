from django.db import models
from user.models import User
from facility.models import Facility
# Create your models here.

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'complaint'


