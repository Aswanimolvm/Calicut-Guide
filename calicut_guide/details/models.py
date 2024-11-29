from django.db import models
from facility.models import Facility
# Create your models here.
class Details(models.Model):
    details_id = models.AutoField(primary_key=True)
    # facility_id = models.IntegerField(blank=True, null=True)
    facility= models.ForeignKey(Facility,to_field='facility_id',on_delete=models.CASCADE)
    address = models.CharField(max_length=450)
    location = models.CharField(max_length=100)
    website_link = models.CharField(db_column='website link', max_length=450)  # Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='phone number', max_length=45)  # Field renamed to remove unsuitable characters.
    details = models.CharField(max_length=1000)
    # status = models.CharField(max_length=45)
    chat = models.CharField(max_length=1000)
    image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details'
