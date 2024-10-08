# Generated by Django 4.2.15 on 2024-08-31 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incident_manager', '0007_incident_district_incident_volunteer'),
        ('volunteer_hub', '0002_volunteer_thana'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='district',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='volunteers', to='incident_manager.district'),
        ),
    ]
