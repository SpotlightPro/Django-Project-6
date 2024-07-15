from django.db import models


# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    qmo_level = models.CharField(max_length=10)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' -  QMO Level: ' + self.qmo_level
