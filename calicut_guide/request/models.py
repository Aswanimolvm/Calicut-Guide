from django.db import models
from user.models import User
from facility.models import Facility

# Create your models here.
class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,to_field='user_id',on_delete=models.CASCADE)
    request = models.CharField(max_length=100)
    location = models.CharField(max_length=25)
    date = models.DateField()
    # facility_id = models.CharField(max_length=45)
    facility=models.ForeignKey(Facility,to_field='facility_id',on_delete=models.CASCADE)
    time = models.TimeField()
    status = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'request'
