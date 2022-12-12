from dataclasses import fields
from django.contrib.auth.hashers import make_password
from cadeMED.models import Clinic, Address, Time, User,  Entity, Specialist, Speciality, Consult, Patient, Schedules

from rest_framework import serializers, validators

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (  'id_address',
                    'state',
                    'city',
                    'district',
                    'zip_code',
                    'house_number',
                    'creat_at',
                    'update_at',
                )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (  'id',
                    'username',
                    'email',
                    'password'
                )   


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = (  'id_entity',
                    'user',
                    'addrres',
                    'name',
                    'phone',
                    'creat_at',
                    'update_at'
            
                )
        
class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Time
        fields = (  'id_time',
                    'date',
                    'time',
                )

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = (  'id_clinic',
                    'cnpj',
                    'entity',
                    'creat_at',
                    'update_at'
                    ) 


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            
            'id_specialist',
            'crm',
            'rqe',
            'creat_at',
            'update_at',
            'id_clinic', 
            'id_speciality',
            'entity'
            
        )      
        
        
        extra_kwargs = {
            
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Specialist.objects.all(), "There is a specialist with this email"
                    )
                ]
            },
            "phone": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Specialist.objects.all(), "There is a specialist with telephone "
                    )
                ]
            }
        }
        
        

        def to_representation(self, instance):
            ret = super().to_representation(instance)
            representation = dict()
            speciality = Speciality.objects.get(pk=ret['id_speciality'])
            clinic = Clinic.objects.get(pk=ret['id_clinic'])
            
            representation['id_specialist'] = ret['id_specialist']
            representation['crm'] = ret['crm']
            representation['rqe'] = ret['rqe']
            representation['creat_at'] = ret['creat_at']
            representation['update_at'] = ret ['update_at']
            
            if speciality is not None:
                representation['id_category'] = category.name
            else:
                representation['id_category'] = ''
                
            return representation
class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = (
        
            'id_speciality',
            'name',
            'creat_at',
            'update_at',
            'description'   
        
        )
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id_patient', 
            'birth_date',
            'entity',
            'creat_at',
            'update_at',
            'cpf'
            
        )
            
        extra_kwargs = {
            "password": {
                "write_only": True,
                "allow_blank": False,
                "style":{
                    'input_type':'password'
                    }
            },
            
            "email": 
                {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Patient.objects.all(), "There is a patient with this email"
                    )
                ]
            },
            
            "phone":{
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Patient.objects.all(), "There is a patient with this phone"
                    )
                ]
            },
            
            "rg":{
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Patient.objects.all(), "There is a patient with this rg"
                    )
                ]
            },
        } 
class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = (
            
            'id_schedules',
            'date_time',
            'creat_at',
            'update_at',
            'canceled',
            'confirmation',
            'comments',
            'id_patient',
            'id_specialist'
            
        )
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        representation = dict()
        patient = Patient.objects.get(pk=ret['id_patient'])
        
        representation ['id_schedules'] = ret['id_schedules']
        representation ['date_time'] = ret['date_time']
        representation ['creat_at'] = ret['creat_at']
        representation ['canceled'] = ret['canceled']
        representation ['confirmation'] = ret['confirmation']
        representation ['comments'] = ret['comments']

        if patient is not None:
            representation['id_patient'] = patient.id_patient
            representation['name'] = patient.name
            representation['city'] = patient.city
            
        return representation

        
class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = (
            
            'id_consult',
            'date_time',
            'creat_at',
            'update_at',
            'symptoms',
            'comments',
            'id_schedules'
            
        )
        


class SchedulesDetailsSerializer(serializers.ModelSerializer):
    historic = ConsultSerializer(many=True, read_only=True)    
    class Meta:
        model = Schedules
        fields = [
            
            'id_schedules',
            'date_time',
            'creat_at',
            'canceled',
            'comments',
            'historic',
            'id_specialist',
            'id_patient'
        ]
        
class PatientDetailsSerializer(serializers.ModelSerializer):
    schedules = SchedulesDetailsSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = [
            
            'id_patient', 
            'name',
            'birth_date', 
            'date_register', 
            'phone', 
            'email', 
            'city', 
            'district',  
            'street',  
            'Num_address',  
            'rg',   
            'schedules',
            'password' 
        
        ]
        
class SpecialistDetaislSerializer(serializers.ModelSerializer):
    detailSpecialist = SchedulesDetailsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Specialist
        fields = [
            
            'id_specialist',
            'name',
            'email',
            'phone',
            'id_clinic',
            'id_speciality',
            'detailSpecialist'
            
            
        ]
        
        
class ClinicDetailSerializer(serializers.ModelSerializer):
    clinics_specialist = SpecialistDetaislSerializer(many=True, read_only=True)
    
    class Meta:
        model = Clinic
        fields = [
    
            'id_clinic',
            'name',
            'email',
            'cnpj',
            'city',
            'phone',
            'district',
            'street',
            'password',
            'clinics_specialist'
            
        ]