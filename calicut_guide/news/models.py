from django.db import models

# Create your models here.
class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=20)
    news = models.CharField(max_length=100)
    location = models.CharField(max_length=25)
    image = models.CharField(max_length=450)
    date = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'news'



