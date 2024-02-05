from rest_framework import serializers
from .models import AssignDevice

class AssignDeviceSerializer(serializers.ModelSerializer):

    device_name = serializers.CharField(source='device.name', read_only=True)
    serial_number = serializers.CharField(source='device.serial_number', read_only=True)
    employee_name = serializers.CharField(source='employee.name', read_only=True)
    employee_designation = serializers.CharField(source='employee.designation', read_only=True)

    class Meta:
        model = AssignDevice
        fields = [
            "device_name",
            "serial_number",
            "employee_name",
            "employee_designation",
            "start_date",
            "end_date",
            "condition_before",
            "condition_after",
            "notes",
            "is_checked_out",
        ]