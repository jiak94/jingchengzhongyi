from django.urls import path
from . import views


app_name = 'appointment'

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/<int:doctor_id>/', views.timeslot, name='timeslot'),
    path('booking/<int:timeslot_id>/', views.booking, name='booking'),
]
