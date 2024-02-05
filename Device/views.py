from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK, HTTP_409_CONFLICT
from .models import Device, AssignDevice
from Company.models import Company, Employee
from .serializer import AssignDeviceSerializer

class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Company').exists()

class IsEmployeeUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Employee').exists()

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
            if 'serial_number' not in data or data['serial_number'] == '':
                result['massage'] = "device_name can not be null."
                result['error'] = "serial_number"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            company = Company.objects.get(company_email=data['company_email'])

            if 'employee_email' in data:
                employee = Employee.objects.get(employee_email=data['employee_email'])
            else:
                employee = None

            device = Device()
            device.name = data['name']
            device.serial_number = data['serial_number']
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


class ApiAssignDevice(CreateAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        result = {}
        try:
            data = request.data
            if 'start_date' not in data or data['start_date'] == '':
                result['massage'] = "start_date can not be null."
                result['error'] = "start_date"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'end_date' not in data or data['end_date'] == '':
                result['massage'] = "end_date can not be null."
                result['error'] = "end_date"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'employee_email' not in data or data['employee_email'] == '':
                result['massage'] = "employee_email can not be null."
                result['error'] = "employee_email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'serial_number' not in data or data['serial_number'] == '':
                result['massage'] = "device_name can not be null."
                result['error'] = "serial_number"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            device = Device.objects.filter(serial_number=data['serial_number']).first()
            employee = Employee.objects.filter(employee_email=data['employee_email']).first()

            if 'is_checked_out' in data and data['is_checked_out'].lower() == "true":

                if device.status == "Assigned":

                    result['status'] = HTTP_409_CONFLICT
                    result['message'] = "Device not available"
                    return Response(result)

                else:
                    assign = AssignDevice()
                    assign.device = device
                    assign.start_date = data['start_date']
                    assign.end_date = data['end_date']
                    assign.condition_before = data['condition_before']
                    assign.notes = data['notes']
                    assign.is_checked_out = True
                    assign.employee = employee
                    assign.save()

                    device.status = "Assigned"
                    device.current_assigned_employee = employee
                    device.save()

                    result['status'] = HTTP_200_OK
                    result['message'] = "Assigned"
                    return Response(result)

            elif 'is_checked_out' in data and data['is_checked_out'].lower() == "false":

                if device.status == "Available":

                    result['status'] = HTTP_409_CONFLICT
                    result['message'] = "Device already returned"
                    return Response(result)

                else:

                    assign = AssignDevice()
                    assign.device = device
                    assign.start_date = data['start_date']
                    assign.end_date = data['end_date']
                    assign.condition_before = data['condition_before']
                    assign.condition_after = data['condition_after']
                    assign.notes = data['notes']
                    assign.is_checked_out = False
                    assign.employee = employee
                    assign.save()

                    device.status = "Available"
                    device.current_assigned_employee = None
                    device.save()

                    result['status'] = HTTP_200_OK
                    result['message'] = "Returned"
                    return Response(result)

        except Exception as ex:
            return Response(str(ex))


class ApiDeviceAssignmentLog(ListAPIView):

    permission_classes = [IsCompanyUser]

    def get(self, request):

        assignmentLog = AssignDevice.objects.all()
        assignmentLog = AssignDeviceSerializer(assignmentLog, many=True).data

        return Response(assignmentLog)