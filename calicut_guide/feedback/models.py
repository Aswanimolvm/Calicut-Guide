from django.db import models
from user.models import User
from facility.models import Facility

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    feedback = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedback'



