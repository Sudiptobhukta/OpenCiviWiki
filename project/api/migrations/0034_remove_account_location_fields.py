# Generated by Django 2.2.16 on 2021-05-03 17:35

import accounts.models
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20190428_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='city',
        ),
        migrations.RemoveField(
            model_name='account',
            name='country',
        ),
        migrations.RemoveField(
            model_name='account',
            name='fed_district',
        ),
        migrations.RemoveField(
            model_name='account',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='account',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='account',
            name='representatives',
        ),
        migrations.RemoveField(
            model_name='account',
            name='state',
        ),
        migrations.RemoveField(
            model_name='account',
            name='state_district',
        ),
        migrations.RemoveField(
            model_name='account',
            name='zip_code',
        ),
    ]
