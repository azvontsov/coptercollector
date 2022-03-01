
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Copter, Kit

# Create your views here.




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def copters_index(request):
    copters = Copter.objects.all()
    return render(request, 'copters/index.html', {'copters': copters})

def copters_detail(request, copter_id):
   copter = Copter.objects.get(id=copter_id)
   charging_form = ChargingForm()

   kits_copter_doesnt_have = Kit.objects.exclude(id__in = copter.kits.all().values_list('id'))

   return render(request, 'copters/detail.html', {
       'copter': copter, 
       'charging_form': charging_form,
       'kits': kits_copter_doesnt_have 
    })


class CopterCreate(CreateView):
    model = Copter
    fields = ['name', 'model', 'price']
    # fields = '__all__'
    # success_url = '/copters/' this will work, but it's not preferred
    # Fat Models, Skinny Controllers

class CopterUpdate(UpdateView):
    model = Copter
    fields = ('name', 'model', 'price')

class CopterDelete(DeleteView):
    model = Copter
    success_url = '/copters/'

class KitCreate(CreateView):
    model = Kit
    fields = ('name', 'price')


class KitUpdate(UpdateView):
    model = Kit
    fields = ('name', 'price')


class KitDelete(DeleteView):
    model = Kit
    success_url = '/kits/'


class KitDetail(DetailView):
    model = Kit
    template_name = 'kits/detail.html'


class KitList(ListView):
    model = Kit
    template_name = 'kits/index.html'