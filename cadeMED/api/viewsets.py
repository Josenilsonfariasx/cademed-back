from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from cadeMED.api import serializers
from cadeMED.api.serializers import TimeSerializer, EntitySerializer, SpecialitySerializer, SpecialistSerializer,AddressSerializer
from cadeMED import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 15

class AddressViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()
class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
class TimeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TimeSerializer
    queryset = models.Time.objects.all()
class EntityViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EntitySerializer
    queryset = models.Entity.objects.all()
class ClinicViweset(viewsets.ModelViewSet):
    serializer_class = serializers.ClinicSerializer
    queryset = models.Clinic.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    search_fields = ['cnpj','id_clinic']
    ordering_fields = ['cnpj','id_clinic']

class SpecialistViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SpecialistSerializer
    queryset = models.Specialist.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['id_speciality','id_clinic']
    ordering_fields = ['id_clinic','id_specialist']

class SpecialityViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SpecialitySerializer
    queryset = models.Speciality.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['id_speciality']
    search_fields = ['id_speciality']
    ordering_fields = ['id_speciality']
class PatientViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PatientSerializer
    queryset = models.Patient.objects.all()
    pagination_class = Pagination

class ConsultViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ConsultSerializer
    queryset = models.Consult.objects.all()
    pagination_class = Pagination    
class SchedulesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SchedulesSerializer
    queryset = models.Schedules.objects.all().order_by('date_time')
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['date_time','id_schedules', 'canceled','confirmation','id_patient','id_specialist']
    search_fields = ['date_time','id_schedules', 'canceled','confirmation','id_patient','id_specialist']
    ordering_fields = ['date_time','id_schedules', 'canceled','confirmation','id_patient','id_specialist']