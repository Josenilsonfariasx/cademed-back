# Generated by Django 4.1.2 on 2022-12-10 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadeMED', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='entity',
            field=models.OneToOneField(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='cadeMED.entity'),
            preserve_default=False,
        ),
    ]