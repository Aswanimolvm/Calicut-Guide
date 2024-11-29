from django.db import models

# Create your models here.

class Organisation(models.Model):
    organisation_id = models.AutoField(primary_key=True)
    organisation_name = models.CharField(db_column='organisation name', max_length=100)  # Field renamed to remove unsuitable characters.
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45)
    lisence_proof = models.CharField(max_length=200)
    e_mail = models.CharField(db_column='e-mail', max_length=45)  # Field renamed to remove unsuitable characters.
    password = models.CharField(max_length=45)
    confirm_password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'organisation'
