from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path('addnewpatient',views.addnewpatient,name="addnewpatient"),
    path('doctorform/<str:prescriptionid>',views.doctorform,name="doctorform"),
    path('prescription/<str:prescriptionid>',views.prescription,name="prescription"),
]