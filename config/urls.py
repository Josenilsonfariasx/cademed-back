from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from cadeMED.api import viewsets
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

route = routers.DefaultRouter()

route.register (r'users', viewsets.UserViewset, basename='Users')
route.register (r'addrress', viewsets.AddressViewset, basename='Addrress')
route.register (r'entity', viewsets.EntityViewset, basename='Entity')
route.register (r'time', viewsets.TimeViewset, basename='Time')
route.register (r'clinic',  viewsets.ClinicViweset,basename='Clinic')
route.register (r'Speciality', viewsets.SpecialityViewset,basename='Speciality')
route.register (r'specialist', viewsets.SpecialistViewset,basename='Specialist')
route.register (r'patient', viewsets.PatientViewset,basename='Patient')
route.register (r'schedules', viewsets.SchedulesViewset,basename='Schedules')
route.register (r'Consult', viewsets.ConsultViewset,basename='Consult')

urlpatterns = [
    path('', include(route.urls))
    
]
