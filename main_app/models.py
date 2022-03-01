from string import digits
from django.db import models
from django.urls import reverse

CHARGES = (
    ('C', 'Charge'),
    ('D', 'Double charge'),
    
)

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

class Charging(models.Model):
    date = models.DateField('charging date')
    charge = models.CharField(max_length=1, choices=CHARGES, default=CHARGES[0][0])
    copter = models.ForeignKey(Copter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_charge_display()} on {self.date}"
        # get_<attribute name>_display()
    class Meta:
        ordering = ('-date', 'charge')

class Photo(models.Model):
    url = models.CharField(max_length=200)
    copter = models.ForeignKey(Copter, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for copter_id: {self.copter_id} @{self.url}"