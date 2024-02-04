from django.db import models

class Company(models.Model):

    name = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):

    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="Employee")
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    employee_phone_number = models.CharField(max_length=255)
    employee_email = models.CharField(max_length=255)