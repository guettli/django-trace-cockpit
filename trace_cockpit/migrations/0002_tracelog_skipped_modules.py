# Generated by Django 3.2.5 on 2021-07-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trace_cockpit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracelog',
            name='skipped_modules',
            field=models.JSONField(default=dict),
        ),
    ]