from django.db import models
from django.urls import reverse

# Create your models here.



class Kit(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"A {self.price} {self.name}"

    def get_absolute_url(self):
        return reverse('kits_detail', kwargs={'pk': self.id})



class Copter(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    kits = models.ManyToManyField(Kit)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'copter_id': self.id})