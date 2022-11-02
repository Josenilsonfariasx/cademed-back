from dataclasses import fields
from django.contrib.auth.hashers import make_password
from cadeMED.models import Clinic, Patient, Schedules, Historic, Category, Specialist

from rest_framework import serializers, validators

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = (  'id_clinic',
                    'name',
                    'email',
                    'cnpj',
                    'state',
                    'city',
                    'phone',
                    'district',
                    'street',
                    'password',
                ) 
        extra_kwargs = {
            "cnpj":{
                "validators":[
                    validators.UniqueValidator(
                        Clinic.objects.all(), "There is a clinic with this CNPJ"
                    )
                ]
            },
            "password": {
                    "write_only": True,
                    "allow_blank": False,
                    "style":{
                    'input_type':'password'
                    }
                        },
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Clinic.objects.all(), "There is a clinic with this EMAIL"
                    )
                ]
            }
        }
        
        def create(self, validated_data):
            clinic = Clinic.objects.create(
                name = validated_data.get('name'),
                email = validated_data.get('email'),    
                password = make_password(validated_data('password'))
            )   
            clinic.set_password(validated_data.get('password'))
            clinic.save()
            return clinic

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            
            'id_specialist', 
            'name_specialist',
            'email',
            'phone',
            'id_clinic', 
            'id_category'
            
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
        
        
        def create(self, validated_data):
            clinic = Clinic.objects.create(
                username = validated_data.get('name'),
                email = validated_data.get('email'),    
                password = validated_data.get('password'),
            )
            clinic.set_password(validated_data.get('password'))
            clinic.save()
            return clinic



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
        
            'id_category',
            'name',
            'description'   
        
        )
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
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
            'password'
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
            'canceled',
            'comments',
            'id_patient',
            'id_specialist'
            
        )
        

        
class HistoricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historic
        fields = (
            
            'id_historic',
            'date',
            'symptoms',
            'description_pain',
            'local_pain',
            'conclusion',
            'id_schedules'
            
        )
        


class SchedulesDetailsSerializer(serializers.ModelSerializer):
    historic = HistoricSerializer(many=True, read_only=True)    
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
            'name_specialist',
            'email',
            'phone',
            'id_clinic',
            'id_category',
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