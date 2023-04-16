# Generated by Django 4.1.7 on 2023-03-20 09:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('birthdate', models.DateField()),
                ('phone_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('location', models.CharField(choices=[('Béja', 'Béja'), ('Ben_Arous', 'Ben Arous'), ('Bizerte', 'Bizerte'), ('Gabés', 'Gabés'), ('Gafsa', 'Gafsa'), ('Jendouba', 'Jendouba'), ('Kairouan', 'Kairouan'), ('Kasserine', 'Kasserine'), ('Kébili', 'Kébili'), ('Ariana', 'Ariana'), ('Manouba', 'Manouba'), ('Mahdia', 'Mahdia'), ('Médinine', 'Médinine'), ('Monastir', 'Monastir'), ('Nabeul', 'Nabeul'), ('Sfax', 'Sfax'), ('Sidi_Bouzid', 'Sidi Bouzid'), ('Siliana', 'Siliana'), ('Sousse', 'Sousse'), ('Tataouine', 'Tataouine'), ('Tozeur', 'Tozeur'), ('Tunis', 'Tunis'), ('Zaghouan', 'Zaghouan'), ('le_Kef', 'le Kef')], max_length=20)),
                ('specialty', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=50)),
                ('landline_number', models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('is_verified', models.BooleanField(default=False, verbose_name='doctor confirmation')),
                ('CustomUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('first_time_visit', models.BooleanField(default=False, verbose_name='first time visit')),
                ('additional_info', models.CharField(blank=True, max_length=100, null=True)),
                ('is_confirmed', models.BooleanField(default=False, verbose_name='doctor confirmation')),
                ('is_rejected', models.BooleanField(default=False, verbose_name='doctor unavailable')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctor')),
            ],
            options={
                'verbose_name': 'appointment',
            },
        ),
    ]
