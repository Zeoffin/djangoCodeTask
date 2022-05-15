from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=30, default="", unique=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"Res-{self.id} {self.rental_id.id}"
