from django.db import models
from user.models import User
from booking.models import Booking
# Create your models here.


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cvv = models.CharField(max_length=20)
    card_holder = models.CharField(max_length=50)
    pay_sts = models.CharField(max_length=50)
    fac_id = models.IntegerField()
    # book_id = models.IntegerField()
    book = models.ForeignKey(Booking, on_delete=models.CASCADE)



    class Meta:
        managed = False
        db_table = 'payment'
