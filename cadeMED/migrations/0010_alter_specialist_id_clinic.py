# Generated by Django 4.1.2 on 2022-10-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadeMED', '0009_alter_clinic_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='id_clinic',
            field=models.ManyToManyField(blank=True, related_name='clinics_specialist', to='cadeMED.clinic'),
        ),
    ]
