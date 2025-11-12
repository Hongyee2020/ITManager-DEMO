# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=255, verbose_name="host_name", unique=True, blank=False)
    ip = models.GenericIPAddressField(verbose_name="IP_address", blank=False)
    disk = models.CharField(max_length=55, null=True, blank=True)
    mem = models.CharField(max_length=55, null=True, blank=True)
    cpu = models.CharField(max_length=55, null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.hostname

    class Meta:
        db_table = "Host"
        ordering = ["hostname"]
        verbose_name = "device"
        verbose_name_plural = "device_List"
