from django.db import models
from auditorium.models import Auditorium
from user.models import User
# Create your models here.


class Rating(models.Model):
    rat_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=100)
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # aud_id = models.IntegerField()
    aud = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'rating'
