# Generated by Django 4.1.2 on 2022-10-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadeMED', '0003_clinic_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='cnpj',
            field=models.CharField(max_length=19),
        ),
    ]
