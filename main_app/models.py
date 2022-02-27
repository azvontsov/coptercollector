from django.db import models
from django.urls import reverse

# Create your models here.

class Copter(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'copter_id': self.id})