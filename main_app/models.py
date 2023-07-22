from django.db import models


class RateModel(models.Model):
    date = models.DateField(unique=True)
    brl = models.FloatField()
    eur = models.FloatField()
    jpy = models.FloatField()

    def __str__(self):
        return f'{self.date}: BRL={self.brl}, EUR={self.eur}, JPY={self.jpy}'
