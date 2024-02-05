from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_409_CONFLICT
from .models import Device
from Company.models import Company, Employee

class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Company').exists()

class ApiAddDevice(CreateAPIView):

    permission_classes = [IsCompanyUser]
    def post(self, request):
        result = {}
        try:
            data = request.data
            if 'name' not in data or data['name'] == '':
                result['massage'] = "Name can not be null."
                result['error'] = "Name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'device_type' not in data or data['device_type'] == '':
                result['massage'] = "device_type can not be null."
                result['error'] = "device_type"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'company_email' not in data or data['company_email'] == '':
                result['massage'] = "company_email can not be null."
                result['error'] = "company_email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'device_model' not in data or data['device_model'] == '':
                result['massage'] = "device_model can not be null."
                result['error'] = "device_model"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'status' not in data or data['status'] == '':
                result['massage'] = "status can not be null."
                result['error'] = "status"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'company_email' not in data or data['company_email'] == '':
                result['massage'] = "company_email can not be null."
                result['error'] = "company_email"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            company = Company.objects.get(company_email=data['company_email'])

            if 'employee_email' in data:
                employee = Employee.objects.get(employee_email=data['employee_email'])
            else:
                employee = None

            device = Device()
            device.name = data['name']
            device.device_type = data['device_type']
            device.device_model = data['device_model']
            device.status = data['status']
            device.condition = data['condition']
            device.company = company
            device.current_assigned_employee = employee
            device.save()

            result['status'] = HTTP_201_CREATED
            result['message'] = "Success"
            result['Device name'] = data['name']
            return Response(result)

        except Exception as ex:
            return Response(str(ex))