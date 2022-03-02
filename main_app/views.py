from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Copter, Kit, Photo
from .forms import ChargingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'coptercollector'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def copters_index(request):
    copters = Copter.objects.all()
    return render(request, 'copters/index.html', {'copters': copters})

@login_required
def copters_detail(request, copter_id):
   copter = Copter.objects.get(id=copter_id)
   charging_form = ChargingForm()

   kits_copter_doesnt_have = Kit.objects.exclude(id__in = copter.kits.all().values_list('id'))

   return render(request, 'copters/detail.html', {
       'copter': copter, 
       'charging_form': charging_form,
       'kits': kits_copter_doesnt_have 
    })

@login_required
def add_charging(request, copter_id):
    
    form = ChargingForm(request.POST)
   
    if form.is_valid():
        
        new_charging = form.save(commit=False)
        
        new_charging.copter_id = copter_id
       
        new_charging.save()
  
    return redirect('detail', copter_id=copter_id)


@login_required
def assoc_kit(request, copter_id, kit_id):
    Copter.objects.get(id=copter_id).kits.add(kit_id)
    return redirect('detail', copter_id=copter_id)

@login_required
def add_photo(request, copter_id):
    
    photo_file = request.FILES.get('photo-file')
    
    
    if photo_file:
        
        s3 = boto3.client('s3')
        
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            #
            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url=url, copter_id=copter_id)
            
            photo.save()
            
        except Exception as error:
            print('An error occurred while uploading to S3')
            print(error)

            
    return redirect('detail', copter_id=copter_id)

def signup(request):
    error_message = ''
    # check for a POST request
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
           
            user = form.save()
            
            login(request, user)
            
            return redirect('index')
        
        else:
            error_message = 'invalid sign up - please try again'
            age
    
    form = UserCreationForm()
    context = { 'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

class CopterCreate(LoginRequiredMixin, CreateView):
    model = Copter
    fields = ['name', 'model', 'price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class CopterUpdate(LoginRequiredMixin, UpdateView):
    model = Copter
    fields = ('name', 'model', 'price')

class CopterDelete(DeleteView):
    model = Copter
    success_url = '/copters/'

class KitCreate(LoginRequiredMixin, CreateView):
    model = Kit
    fields = ('name', 'price')


class KitUpdate(LoginRequiredMixin, UpdateView):
    model = Kit
    fields = ('name', 'price')


class KitDelete(LoginRequiredMixin, DeleteView):
    model = Kit
    success_url = '/kits/'


class KitDetail(LoginRequiredMixin, DetailView):
    model = Kit
    template_name = 'kits/detail.html'


class KitList(LoginRequiredMixin, ListView):
    model = Kit
    template_name = 'kits/index.html'