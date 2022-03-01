from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Copter, Kit, Photo
from .forms import ChargingForm

import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'coptercollector-az'

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

def add_charging(request, copter_id):
    # 1) collect form input values
    form = ChargingForm(request.POST)
    # 2) valid input values
    if form.is_valid():
        # 3) save a copy of a new charging instance in memory
        new_charging = form.save(commit=False)
        # 4) attach a reference to the copter that owns the charging
        new_charging.copter_id = copter_id
        # 5) save the new charging to the database
        new_charging.save()
    # 6) redirect the user back to the detail
    return redirect('detail', copter_id=copter_id)

# Renders a template with a form on it
# Creates a model form based on the model
# Responds to GET and POST requests
#  1) GET render the new copter form
#  2) POST submit the form to create a new instance
# Validate form inputs
# Handles the necessary redirect following a model instance creating

def assoc_kit(request, copter_id, kit_id):
    Copter.objects.get(id=copter_id).kits.add(kit_id)
    return redirect('detail', copter_id=copter_id)

def add_photo(request, copter_id):
    # attempt to collect the photo information from the form submission
    photo_file = request.FILES.get('photo-file')
    # use an if statement to see if the photo information is present or not
    # if photo present
    if photo_file:
        # initialize a reference to the s3 service from boto3
        s3 = boto3.client('s3')
        # create a unique name for the photo asset
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # attempt to upload the photo asset to AWS S3
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # Save a secure url to the AWS S3 hosted photo asset to the database
            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url=url, copter_id=copter_id)
            
            photo.save()
            # if upload is not successful
        except Exception as error:
            print('An error occurred while uploading to S3')
            print(error)

            # print errors to the console
        # return a response as a redirect to the client - redirecting to the detail page
    return redirect('detail', copter_id=copter_id)



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