# Generated by Django 4.1.2 on 2022-12-11 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadeMED', '0002_alter_clinic_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='entity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cadeMED.entity'),
        ),
    ]