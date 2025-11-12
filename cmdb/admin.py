# 导入 Django 自带的后台管理模块，用于管理数据库模型的增删改查。
from django.contrib import admin
# 当前应用的 models.py 文件导入名为 Host 的模型（通常对应数据库中的一张表）。
from cmdb.models import Host
from cmdb.models import Reactor,Reactor3333

# 定义一个自定义管理类 HostAdmin，继承 Django 的 admin.ModelAdmin 基类。
# 作用：定制 Host 模型在后台管理界面的显示方式。
class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'ip', 'cpu', 'mem', 'disk', 'desc']

class ReactorAdmin(admin.ModelAdmin):
    list_display = ['name', 'volume_m3', 'volume_m3', 'volume_m3', 'volume_m3', 'volume_m3']
# 核心功能：将 Host 模型注册到 Django 后台管理界面。
# 参数：
# Host：要注册的模型
# HostAdmin：关联的自定义管理配置类（指定显示方式）
admin.site.register(Host, HostAdmin)
admin.site.register(Reactor, ReactorAdmin)
admin.site.register(Reactor3333, ReactorAdmin)