from django.contrib import admin
from .models import Copter, Charging, Kit, Photo

admin.site.register(Copter)
admin.site.register(Charging)
admin.site.register(Kit)
admin.site.register(Photo)

