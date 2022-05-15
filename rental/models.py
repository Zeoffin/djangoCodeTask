from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=30, default="")


class Reservation(models.Model):
    rental_id = models.IntegerField()
    checkin = models.DateField()
    checkout = models.DateField()
