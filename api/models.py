# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Abrahammr(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    comentarios = models.CharField(max_length=300, blank=True, null=True)
    creacion = models.DateTimeField(blank=True, default=timezone.now,  null=True)
    actualizacion = models.DateTimeField(blank=True, default=timezone.now, null=True)

    class Meta:
        managed = False
        db_table = 'abrahammr'
