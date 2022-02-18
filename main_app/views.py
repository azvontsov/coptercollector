from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
class Copter:
    def __init__(self, name, model, description, price):
        self.name = name
        self.model = model
        self.description = description
        self.price = price

copters = [ 
    Copter('DJI', 'Mavic 3', 'superduper', 1000),
    Copter('DJI', 'Fantom', 'mega photo', 2000),
    Copter('RUKO', 'F11Pro', 'fast', 800),
]




def home(request):
    return HttpResponse('<h1>Hi</h1>')

def about(request):
    return render(request, 'about.html')

def copters_index(request):
    return render(request, 'copters/index.html', { 'copters' : copters})
