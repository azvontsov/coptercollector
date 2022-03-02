from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('copters/', views.copters_index, name='index'),
    path('copters/<int:copter_id>/', views.copters_detail, name='detail'),
    path('copters/create/', views.CopterCreate.as_view(), name='copters_create'),
    path('copters/<int:pk>/update/', views.CopterUpdate.as_view(), name='copters_update'),
    path('copters/<int:pk>/delete/', views.CopterDelete.as_view(), name='copters_delete'),
    path('copters/<int:copter_id>/add_charging/', views.add_charging, name='add_charging'),
    path('kits/', views.KitList.as_view(), name='kits_index'),
    path('kits/<int:pk>/', views.KitDetail.as_view(), name='kits_detail'),
    path('kits/create/', views.KitCreate.as_view(), name='kits_create'),
    path('kits/<int:pk>/update/', views.KitUpdate.as_view(), name='kits_update'),
    path('kits/<int:pk>/delete/', views.KitDelete.as_view(), name='kits_delete'),
    path('copters/<int:copter_id>/assoc_kit/<int:kit_id>/', views.assoc_kit, name='assoc_kit'),
    path('copters/<int:copter_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),   
]