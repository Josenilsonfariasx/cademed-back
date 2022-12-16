from dataclasses import fields
from django.contrib.auth.hashers import make_password
from cadeMED.models import Clinic, Address, Time, User,  Entity, Specialist, Speciality, Consult, Patient, Schedules
from uuid import uuid4

from rest_framework import serializers, validators

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (  'id_address',
                    'state',
                    'city',
                    'district',
                    'street',
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

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        representation = dict()
        user = Clinic.objects.get(pk=ret['id_clinic'])
        
        representation['id_clinic'] = ret['id_clinic']
        representation['cnpj'] = ret['cnpj']
        representation['creat_at'] = ret['creat_at']
        representation['update_at'] = ret['update_at']
        
        if user is not None:
            representation['name_clinic'] = user.entity.name
            representation['phone_clinic'] = user.entity.phone
            representation['city_clinic'] = user.entity.addrres.city
            representation['street_clinic'] = user.entity.addrres.street
        else:
            representation['name_clinic']  = ''
            representation['phone_clinic'] = ''
            representation['city_clinic']  = ''
            representation['street_clinic']= ''
        
        return representation
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
        # clinic = Clinic.objects.get(pk = ret['id_clinic'])
        
        representation['id_specialist'] = ret['id_specialist']
        representation['crm'] = ret['crm']
        representation['rqe'] = ret['rqe']
        representation['creat_at'] = ret['creat_at']
        representation['update_at'] = ret ['update_at']
        representation['entity'] = ret ['entity']
        representation['id_clinic'] = ret['id_clinic']
        
        # if clinic is not None:
        #     representation['id_clinic'] = clinic.id_clinic
        #     representation['name_clinic'] = clinic.entity.name
        # else:
        #     representation['id_clinic'] = ''
        #     representation['name_clinic'] = ''
        if speciality is not None:
            representation['id_speciality'] = speciality.id_speciality
            representation['name_speciality'] = speciality.name
        else:
            representation['id_speciality'] = ''
        # def to_representation(self, instance):
        #     ret = super().to_representation(instance)aaaa
        #     representation = dict()
        #     category = Category.objects.get(id=ret['id_category'])
            
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
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        representation = dict()
        user = Patient.objects.get(pk = ret['id_patient'])
        
        representation['id_patient'] = ret['id_patient']
        representation['birth_date'] = ret['birth_date']
        representation['creat_at'] = ret['creat_at']
        representation['update_at'] = ret['update_at']
        representation['cpf'] = ret['cpf']
        
        if user is not None:
            representation['name_patient'] = user.entity.name
            representation['phone_patient'] = user.entity.phone
            representation['city_patient'] = user.entity.addrres.city
            representation['street_patient'] = user.entity.addrres.street
        
        return representation
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
        specialist = Specialist.objects.get(pk=ret['id_specialist'])
        
        representation ['id_schedules'] = ret['id_schedules']
        representation ['date_time'] = ret['date_time']
        representation ['creat_at'] = ret['creat_at']
        representation ['canceled'] = ret['canceled']
        representation ['confirmation'] = ret['confirmation']
        representation ['comments'] = ret['comments']
        representation ['id_specialist'] = ret ['id_specialist']

        if specialist is not None:
            representation['id_specialist'] = specialist.entity.name
            representation['clinic_specialist'] = specialist.id_clinic.name
        else:
            representation['clinic_specialist'] = ''
        if patient is not None:
            representation['id_patient'] = patient.id_patient
            representation['name_patient'] = patient.entity.name
            representation['city_patient'] = patient.entity.addrres.city
        else:
            representation['id_patient'] = ''
            representation['name'] = ''
            representation['city'] = ''
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
        fields = (
            'id_schedules',
            'date_time',
            'creat_at',
            'canceled',
            'comments',
            'historic',
            'id_specialist',
            'id_patient'
        )
        
# class PatientDetailsSerializer(serializers.ModelSerializer):
#     schedules = SchedulesDetailsSerializer(many=True, read_only=True)
#     class Meta:
#         model = Patient
#         fields = [
            
#             'id_patient', 
#             'birth_date',  
#             'cpf',
#             'schedules'
        
#         ]
        
# class SpecialistDetaislSerializer(serializers.ModelSerializer):
#     detailSpecialist = SchedulesDetailsSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Specialist
#         fields = [
            
#             'id_specialist',
#             'id_clinic',
#             'id_speciality',
#             'detailSpecialist'
            
            
#         ]
        
        
# class ClinicDetailSerializer(serializers.ModelSerializer):
#     clinics_specialist = SpecialistDetaislSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Clinic
#         fields = [
    
#             'id_clinic',
#             'cnpj',
#             'clinics_specialist'
            
#         ]