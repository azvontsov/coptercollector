from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('copters/', views.copters_index, name='index'),
    path('copters/<int:copter_id>', views.copters_detail, name='detail'),
]