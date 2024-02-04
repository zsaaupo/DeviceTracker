from django.contrib import admin
from .models import Device, AssignDevice


class DeviceAdmin(admin.ModelAdmin):

    fields = [
        "company",
        "name",
        "device_type",
        "device_model",
        "status",
        "condition",
        "current_assigned_employee"
    ]

    list_display = [
        "name",
        "device_type",
        "device_model"
    ]

admin.site.register(Device,DeviceAdmin)


class AssignDeviceAdmin(admin.ModelAdmin):

    fields = [
        "device",
        "employee",
        "start_date",
        "end_date",
        "condition_before",
        "condition_after",
        "notes"
    ]

    list_display = [
        "device",
        "employee"
    ]

admin.site.register(AssignDevice,AssignDeviceAdmin)