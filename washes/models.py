from django.db import models

# Create your models here.

class CarWash(models.Model):
    title = models.CharField(max_length=200)
    # region =
    added = models.DateField(auto_now_add=True)
    rating = models.FloatField()
    location_data = models.JSONField()
    # brand =

    def __str__(self):
        return f'{self.title}'

