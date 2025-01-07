# Generated by Django 5.1.4 on 2025-01-06 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctorprofile', '0001_initial'),
        ('patientfilesystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.DateTimeField()),
                ('consultation_type', models.CharField(choices=[('in_person', 'In Person'), ('voice', 'Voice Call'), ('video', 'Video Call')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorprofile.doctorprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientfilesystem.patient')),
            ],
        ),
    ]
