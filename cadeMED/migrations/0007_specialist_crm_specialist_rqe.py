# Generated by Django 4.1.2 on 2022-10-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadeMED', '0006_alter_schedules_id_patient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='crm',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialist',
            name='rqe',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]