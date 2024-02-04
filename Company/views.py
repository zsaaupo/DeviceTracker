from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_409_CONFLICT
from django.contrib.auth.hashers import make_password
from .models import Company


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

            user = User.objects.filter(username=data['email']).first()

            if user:
                result['status']=HTTP_409_CONFLICT
                result['message']="Company is already exist"
                return Response(result)

            if not user:

                company_group, created = Group.objects.get_or_create(name='Company')

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