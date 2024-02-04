# Generated by Django 5.0.1 on 2024-02-04 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_phone_number', models.CharField(max_length=11)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('employee_phone_number', models.CharField(max_length=255)),
                ('employee_email', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Employee', to='Company.company')),
            ],
        ),
    ]
