from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from cadeMED.api import serializers
from cadeMED.api.serializers import PatientDetailsSerializer, SchedulesDetailsSerializer, CategorySerializer, SpecialistDetaislSerializer, SpecialistSerializer, ClinicDetailSerializer
from cadeMED import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 15

class ClinicViweset(viewsets.ModelViewSet):
    serializer_class = serializers.ClinicSerializer
    queryset = models.Clinic.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['city','state']
    search_fields = ['name','id_clinic','city','state']
    ordering_fields = ['name','id_clinic','city','state']
    
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
    
    filterset_fields = ['name_specialist','id_category','id_clinic']
    search_fields = ['name_specialist','email']
    ordering_fields = ['name_specialist','id_clinic','id_specialist']
    
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args,**kwargs):
        self.serializer_class = SpecialistDetaislSerializer
        queryset = models.Specialist.objects.filter(pk=pk)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)
    
class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['name','id_category']
    search_fields = ['name','id_category']
    ordering_fields = ['name','id_category']
    
class PatientViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PatientSerializer
    queryset = models.Patient.objects.all().order_by('name')
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
        
class HistoricViewset(viewsets.ModelViewSet):
    serializer_class = serializers.HistoricSerializer
    queryset = models.Historic.objects.all().order_by('date')
    pagination_class = Pagination