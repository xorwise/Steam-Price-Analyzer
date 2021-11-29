from django.db import models

# Create your models here.
class Skin(models.Model):
    name = models.CharField(max_length=200)
    # lowest_price = models.FloatField(blank=True)
    # highest_price = models.FloatField(blank=True)
    current_price = models.CharField(max_length=200, blank=True)
    # prev_prices = models.TextField()

    def __str__(self):
        return self.name