from django.contrib import admin
from .models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):

    fields = [
        "user",
        "name",
        "company_email",
        "company_phone_number",
        "address"
    ]

    list_display = ["name"]

admin.site.register(Company,CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):

    fields = [
        "user",
        "company",
        "name",
        "designation",
        "employee_phone_number",
        "employee_email"
    ]

    list_display = [
        "name",
        "designation"
    ]

admin.site.register(Employee,EmployeeAdmin)