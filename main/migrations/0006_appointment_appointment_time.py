# Generated by Django 4.1.7 on 2023-03-26 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_appointment_doctor_proposed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_time',
            field=models.TimeField(null=True),
        ),
    ]
