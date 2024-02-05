from django.db import models
from Company.models import Company, Employee
from .string import status

class Device(models.Model):

    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="Device")
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    device_type = models.CharField(max_length=255)
    device_model = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=(("Available", "Available"), ("Assigned", "Assigned"),("Under repair", "Under repair")), default="Available")
    condition = models.TextField(null=True, blank=True)
    current_assigned_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name="current_devices")

    def __str__(self):
        return self.name + " " + self.serial_number + " " + self.device_type

class AssignDevice(models.Model):

    device = models.ForeignKey(Device, on_delete=models.PROTECT, related_name="assignments", null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="assignments", null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_checked_out = models.BooleanField(null=True, blank=True)
    condition_before = models.TextField(null=True, blank=True)
    condition_after = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
