from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('copters/', views.copters_index, name='index'),
    path('copters/<int:copter_id>', views.copters_detail, name='detail'),
    path('copters/create/', views.CopterCreate.as_view(), name='copters_create'),
    path('copters/<int:pk>/update/', views.CopterUpdate.as_view(), name='copters_update'),
    path('copters/<int:pk>/delete/', views.CopterDelete.as_view(), name='copters_delete'),

]