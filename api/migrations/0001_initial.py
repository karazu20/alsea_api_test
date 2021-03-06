# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-22 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abrahammr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=300, null=True)),
                ('creacion', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('actualizacion', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'abrahammr',
                'managed': False,
            },
        ),
    ]
