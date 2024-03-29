# Generated by Django 4.1.2 on 2022-12-17 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id_address', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=9)),
                ('house_number', models.IntegerField()),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id_clinic', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cnpj', models.CharField(max_length=19)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id_entity', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('addrres', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cadeMED.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_patient', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=16)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='cadeMED.entity')),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id_speciality', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id_time', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id_specialist', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('crm', models.CharField(max_length=12)),
                ('rqe', models.CharField(max_length=12)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entity_specialy', to='cadeMED.entity')),
                ('id_clinic', models.ManyToManyField(blank=True, related_name='clinics_specialists', to='cadeMED.clinic')),
                ('id_speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Speciality_Specialists', to='cadeMED.speciality')),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id_schedules', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('canceled', models.BooleanField(default=False)),
                ('confirmation', models.BooleanField(default=False)),
                ('comments', models.TextField()),
                ('id_patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='cadeMED.patient')),
                ('id_specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detailSpecialist', to='cadeMED.specialist')),
            ],
            options={
                'unique_together': {('date_time', 'id_patient')},
            },
        ),
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id_consult', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('symptoms', models.CharField(blank=True, max_length=200, null=True)),
                ('comments', models.TextField()),
                ('id_schedules', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historic', to='cadeMED.schedules')),
            ],
        ),
        migrations.AddField(
            model_name='clinic',
            name='entity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cadeMED.entity'),
        ),
        migrations.AlterUniqueTogether(
            name='clinic',
            unique_together={('cnpj', 'id_clinic')},
        ),
    ]
