from django.db import models

class Bond(models.Model):
    bond_number = models.CharField(max_length=50)
    draw_date = models.DateField()
    denomination = models.DecimalField(max_digits=10, decimal_places=2)
    prize_won = models.DecimalField(max_digits=10, decimal_places=2)
