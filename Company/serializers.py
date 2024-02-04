from rest_framework import serializers
from .models import Company
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:

        model = Company
        fields = [
            "name",
            "email",
            "phone",
            "address"
        ]