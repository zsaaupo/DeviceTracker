# Generated by Django 5.0.1 on 2024-02-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0005_rename_id_checked_out_assigndevice_is_checked_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='serial_number',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]