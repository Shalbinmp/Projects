from django.db import models

# Create your models here.


class Auditorium(models.Model):
    aud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'auditorium'
