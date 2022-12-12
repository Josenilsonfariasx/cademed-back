from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from cadeMED.api import serializers
from cadeMED.api.serializers import PatientDetailsSerializer,TimeSerializer, EntitySerializer, SchedulesDetailsSerializer, SpecialitySerializer, SpecialistDetaislSerializer, SpecialistSerializer, ClinicDetailSerializer, AddressSerializer
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
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs ):
        self.serializer_class = ClinicDetailSerializer
        queryset = models.Clinic.objects.filter(pk=pk)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)
class SpecialistViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SpecialistSerializer
    queryset = models.Specialist.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['id_speciality','id_clinic']
    search_fields = ['email']
    ordering_fields = ['id_clinic','id_specialist']
    
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args,**kwargs):
        self.serializer_class = SpecialistDetaislSerializer
        queryset = models.Specialist.objects.filter(pk=pk)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)
class SpecialityViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SpecialitySerializer
    queryset = models.Speciality.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['name','id_speciality']
    search_fields = ['name','id_speciality']
    ordering_fields = ['name','id_speciality']
class PatientViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PatientSerializer
    queryset = models.Patient.objects.all()
    pagination_class = Pagination
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        self.serializer_class = PatientDetailsSerializer
        queryset = models.Patient.objects.filter(pk=pk)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)
class SchedulesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.SchedulesSerializer
    queryset = models.Schedules.objects.all().order_by('date_time')
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['date_time','id_schedules']
    search_fields = ['date_time','id_schedules','id_patient']
    ordering_fields = ['date_time','id_schedules']
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = models.Schedules.objects.filter(pk=pk)
        self.serializer_class = SchedulesDetailsSerializer
        serializer = self.get_serializer(queryset ,many=True)
        
        return Response(serializer.data)
class ConsultViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ConsultSerializer
    queryset = models.Consult.objects.all()
    pagination_class = Pagination