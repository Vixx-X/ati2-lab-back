from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from back.apps.client.serializers import ClientSerializer

from .models import Business, Employee, Provider, ProviderRepresentant


class BusinessSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Business
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class ProviderRepresentantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderRepresentant
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    representant = ProviderRepresentantSerializer()

    class Meta:
        model = Provider
        fields = "__all__"
