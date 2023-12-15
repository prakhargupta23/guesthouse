from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
# class User(AbstractUser):
#     is_email_verified = models.BooleanField(default=False)




class Reviews(models.Model):
    name = models.CharField(max_length=122)
    txt = models.TextField()

    def __str__(self):
        return self.name


class Bookingreq(models.Model):
    name = models.CharField(max_length=122)
    chckindate = models.DateField()
    chckoutdate = models.DateField()
    purpose = models.TextField()    
    roomtype = models.TextField()
    noofrooms = models.IntegerField()
    tcost = models.IntegerField(default=500,validators=[MaxValueValidator(10000)])
    rstatus = models.TextField(default='pending')

    def __str__(self):
        return self.name
   
class Room(models.Model):
    type = models.CharField(max_length=122)
    price = models.IntegerField()
    numsofroom = models.IntegerField(default=5)


    def __str__(self):
        return self.type