from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Copter

# Create your views here.





def home(request):
    return HttpResponse('<h1>Hi</h1>')

def about(request):
    return render(request, 'about.html')


def copters_index(request):
    copters = Copter.objects.all()
    return render(request, 'copters/index.html', { 'copters': copters })

def copters_detail(request, copter_id):
    copter = Copter.objects.get(id=copter_id)
    return render(request, 'copters/detail.html', { 'copter' : copter })



class CopterCreate(CreateView):
    model = Copter
    fields = ['name', 'model', 'description', 'price']

class CopterUpdate(UpdateView):
    model = Copter
    fields = ['name', 'model', 'description', 'price']
class CopterDelete(DeleteView):
    model = Copter
    success_url = '/copters/'