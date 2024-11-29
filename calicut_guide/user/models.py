from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    age = models.IntegerField()
    gender = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    locationl = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    id_proof = models.CharField(db_column='ID_proof', max_length=200)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    e_mail = models.CharField(db_column='e-mail', max_length=45)  # Field renamed to remove unsuitable characters.
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'

