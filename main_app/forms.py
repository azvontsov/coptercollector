from dataclasses import field
from django.forms import ModelForm
from .models import Charging

class ChargingForm(ModelForm):
    class Meta:
        model = Charging
        fields = ('date', 'charge')
