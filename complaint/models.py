from django.db import models
from auditorium.models import Auditorium
from user.models import User
# Create your models here.


class Complaint(models.Model):
    comp_id = models.AutoField(primary_key=True)
    # aud_id = models.IntegerField()
    aud=models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'complaint'
