from django.db import models
from user.models import User
from facilities.models import Facilities
from auditorium.models import Auditorium
# Create your models here.


class Booking(models.Model):
    book_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)
    reminders = models.CharField(max_length=100)
    # fac_id = models.IntegerField()
    fac = models.ForeignKey(Facilities, on_delete=models.CASCADE)
    # aud_id = models.IntegerField()
    aud = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    book_sts = models.CharField(max_length=50)



    class Meta:
        managed = False
        db_table = 'booking'
