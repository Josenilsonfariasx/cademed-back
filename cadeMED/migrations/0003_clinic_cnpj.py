# Generated by Django 4.1.2 on 2022-10-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadeMED', '0002_rename_name_specialist_name_specialist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='cnpj',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
    ]
