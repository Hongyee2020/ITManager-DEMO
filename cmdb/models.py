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

class Reactor(models.Model):
    name = models.CharField("反应釜名称", max_length=100)
    volume_m3 = models.FloatField("容积 (m³)")
    material = models.CharField("材质", max_length=50, default="不锈钢316L")
    pressure_bar = models.FloatField("设计压力 (bar)", null=True, blank=True)
    temperature_c = models.IntegerField("设计温度 (°C)", null=True, blank=True)
    install_date = models.DateField("安装日期", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "反应釜"
        verbose_name_plural = "反应釜列表"

class Reactor3333(models.Model):
    name = models.CharField("反应釜名称", max_length=100)
    volume_m3 = models.FloatField("容积 (m³)")
    material = models.CharField("材质", max_length=50, default="不锈钢316L")
    pressure_bar = models.FloatField("设计压力 (bar)", null=True, blank=True)
    temperature_c = models.IntegerField("设计温度 (°C)", null=True, blank=True)
    install_date = models.DateField("安装日期", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Reactor3333"
        verbose_name = "反应釜"
        verbose_name_plural = "反应釜列表"