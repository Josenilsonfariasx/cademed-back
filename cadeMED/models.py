from datetime import datetime
from django.contrib.auth.models import User
from uuid import uuid4
from django.db import models

from uuid import uuid4

class Address(models.Model):
    id_address = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=9)
    house_number = models.IntegerField()
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.state

class Entity(models.Model):
    id_entity = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    addrres = models.OneToOneField(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Time(models.Model):
    id_time = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField()
    
class Clinic(models.Model):
    id_clinic  = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cnpj = models.CharField(max_length=19, blank=False, null=False)
    entity = models.OneToOneField(Entity, on_delete=models.CASCADE)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.entity.name
    class Meta:
        unique_together = ('cnpj','id_clinic')
        
        
class Speciality(models.Model):
    id_speciality = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Specialist(models.Model):
    id_specialist = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    crm = models.CharField(max_length=12, blank=False, null=False)
    rqe = models.CharField(max_length=12, blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    id_clinic = models.ManyToManyField(Clinic, related_name='clinics_specialists', blank=True)
    id_speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='Speciality_Specialists')
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='entity_specialy', blank=True, null=True)
    
    def __str__(self):
        return self.entity.name
class Patient(models.Model):
    id_patient = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cpf = models.CharField(max_length=16)
    birth_date = models.DateTimeField(blank=True, null=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='patients', blank=True, null=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
class Schedules(models.Model):
    id_schedules = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date_time = models.DateTimeField(blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    canceled = models.BooleanField(default=False)
    confirmation = models.BooleanField(default=False)
    comments = models.TextField()
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='schedules', blank=True, null=True)
    id_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='detailSpecialist', blank=False, null=False)
    
    
    def __str__(self):
        name = self.id_patient.name
        return name
    class Meta:
        unique_together = ('date_time', 'id_patient')
        
class Consult(models.Model):
    id_consult = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date_time = models.DateTimeField(auto_now_add=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    symptoms = models.CharField(max_length=200, blank=True, null=True)
    comments = models.TextField()
    id_schedules = models.ForeignKey(Schedules, related_name='historic', on_delete=models.CASCADE, blank=False, null=True )
    