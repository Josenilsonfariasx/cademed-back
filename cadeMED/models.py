from datetime import datetime
from tokenize import blank_re
from unicodedata import category
from uuid import uuid4
from django.db import models

from uuid import uuid4
class Clinic(models.Model):
    id_clinic  = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cnpj = models.CharField(max_length=19, blank=False, null=False)
    name  = models.CharField(max_length=300)
    email = models.EmailField(max_length=400)
    state = models.CharField(max_length=20, blank=False, null=False)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, unique=True, blank=True, null=True)   
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    password = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('cnpj','name')
        
class Category(models.Model):
    id_category = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Specialist(models.Model):
    id_specialist = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_specialist = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    crm = models.CharField(max_length=12, blank=False, null=False)
    rqe = models.CharField(max_length=12, blank=False, null=False)
    id_clinic = models.ManyToManyField(Clinic, related_name='clinics_specialist', blank=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorySpecialist')
    
    def __str__(self):
        return self.name_specialist
    
class Patient(models.Model):
    id_patient = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300)
    birth_date = models.DateTimeField(blank=True, null=True)
    date_register = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=11, unique=True, blank=True, null=True)   
    email = models.EmailField(max_length=400)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    Num_address = models.IntegerField(blank=True)
    rg = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    

class Schedules(models.Model):
    id_schedules = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date_time = models.DateTimeField(blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    canceled = models.BooleanField(default=False)
    comments = models.TextField()
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='schedules', blank=True, null=True)
    id_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='detailSpecialist', blank=False, null=False)
    
    
    def __str__(self):
        name = self.id_patient.name
        return name
    class Meta:
        unique_together = ('date_time', 'id_patient')
        
class Historic(models.Model):
    id_historic = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    symptoms = models.CharField(max_length=200, blank=True, null=True)
    description_pain = models.TextField(max_length=150, blank=True, null=True)
    local_pain = models.CharField(max_length=100, blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    id_schedules = models.ForeignKey(Schedules, related_name='historic', on_delete=models.CASCADE, blank=False, null=True )
    