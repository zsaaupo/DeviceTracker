from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_409_CONFLICT
from django.contrib.auth.hashers import make_password
from .models import Company, Employee


class ApiCreateCompany(CreateAPIView):
    permission_classes = []
    def post(self, request):
        result = {}
        try:
            data = request.data
            if 'name' not in data or data['name'] == '':
                result['massage'] = "Name can not be null."
                result['error'] = "Name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'email' not in data or data['email'] == '':
                result['massage'] = "Email can not be null."
                result['error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'phone' not in data or data['phone'] == '':
                result['massage'] = "Phone can not be null."
                result['error'] = "Phone"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'address' not in data or data['address'] == '':
                result['massage'] = "Address date can not be null."
                result['error'] = "Address"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['massage'] = "Password can not be null."
                result['error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()

            if user:
                result['status']=HTTP_409_CONFLICT
                result['message']="Company is already exist"
                return Response(result)

            if not user:

                company_group, created = Group.objects.get_or_create(name='Company')

                if not company_group.permissions.all():
                    employee_permission_codenames = ['add_employee', 'change_employee', 'delete_employee', 'view_employee']
                    employee_permissions = Permission.objects.filter(codename__in=employee_permission_codenames)

                    device_permission_codenames = ['add_device', 'change_device', 'delete_device', 'view_device']
                    device_permissions = Permission.objects.filter(codename__in=device_permission_codenames)

                    assign_device_permission_names = ['Can add assign device', 'Can change assign device', 'Can delete assign device', 'Can view assign device']
                    assign_device_permissions = Permission.objects.filter(name__in=assign_device_permission_names)

                    company_group.permissions.add(*employee_permissions)
                    company_group.permissions.add(*device_permissions)
                    company_group.permissions.add(*assign_device_permissions)
                    company_group.save()

                user = User()
                user.username = data['email']
                user.first_name = data['name']
                user.password = make_password(data['password'])
                user.is_active = True
                user.is_staff = True
                user.save()
                user.groups.add(company_group)

                company = Company()
                company.user = user
                company.name = data['name']
                company.company_email = data['email']
                company.company_phone_number = data['phone']
                company.address = data['address']
                company.save()

                result['status']=HTTP_201_CREATED
                result['message']="Success"
                result['Company Name']=data['name']
                return Response(result)

        except Exception as ex:
            return Response(str(ex))

class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Company').exists()


class ApiNewEmployee(CreateAPIView):

    permission_classes = [IsCompanyUser]
    def post(self, request):
        result = {}
        try:
            data = request.data
            if 'name' not in data or data['name'] == '':
                result['massage'] = "name can not be null."
                result['error'] = "name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'email' not in data or data['email'] == '':
                result['massage'] = "Email can not be null."
                result['error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'phone' not in data or data['phone'] == '':
                result['massage'] = "Phone can not be null."
                result['error'] = "Phone"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'designation' not in data or data['designation'] == '':
                result['massage'] = "designation can not be null."
                result['error'] = "designation"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'company_email' not in data or data['company_email'] == '':
                result['massage'] = "company_email can not be null."
                result['error'] = "company_email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['massage'] = "Password can not be null."
                result['error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)


            user = User.objects.filter(username=data['email']).first()

            if user:
                result['status']=HTTP_409_CONFLICT
                result['message']="Employee is already exist"
                return Response(result)

            if not user:

                try:
                    company = Company.objects.get(company_email=data['company_email'])
                except Company.DoesNotExist:
                    result['status'] = HTTP_400_BAD_REQUEST
                    result['message'] = "Company with the given email does not exist."
                    return Response(result, status=result['status'])

                employee_group, created = Group.objects.get_or_create(name='Employee')

                if not employee_group.permissions.all():

                    device_permission_codenames = ['view_device']
                    device_permissions = Permission.objects.filter(codename__in=device_permission_codenames)

                    assign_device_permission_names = ['Can add assign device', 'Can change assign device', 'Can delete assign device', 'Can view assign device']
                    assign_device_permissions = Permission.objects.filter(name__in=assign_device_permission_names)

                    employee_group.permissions.add(*device_permissions)
                    employee_group.permissions.add(*assign_device_permissions)
                    employee_group.save()

                user = User()
                user.username = data['email']
                user.first_name = data['name']
                user.password = make_password(data['password'])
                user.is_active = True
                user.is_staff = True
                user.save()
                user.groups.add(employee_group)

                employee = Employee()
                employee.user = user
                employee.company = company
                employee.name = data['name']
                employee.employee_email = data['email']
                employee.employee_phone_number = data['phone']
                employee.designation = data['designation']
                employee.save()

                result['status']=HTTP_201_CREATED
                result['message']="Success"
                result['Company Name']=data['company_email']
                return Response(result)

        except Exception as ex:
            return Response(str(ex))