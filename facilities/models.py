from django.db import models
from auditorium.models import Auditorium
# Create your models here.


class Facilities(models.Model):
    fac_id = models.AutoField(primary_key=True)
    facilities = models.CharField(max_length=100)
    # aud_id = models.IntegerField()
    aud=models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)


    class Meta:
        managed = False
        db_table = 'facilities'
