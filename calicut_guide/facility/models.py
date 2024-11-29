from django.db import models
from user.models import User

# Create your models here.

class Facility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    facility_type = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    image = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    organisation_id = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'facility'


