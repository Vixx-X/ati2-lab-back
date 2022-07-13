from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from back.apps.client.serializers import ClientSerializer
from back.apps.user.serializers import UserEmployeeSerializer

from back.core.serializers import GenericSerializer
from .models import Business, Employee, Provider, ProviderRepresentant


class BusinessSerializer(GenericSerializer):
    client = ClientSerializer(source='get_client')

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            for field in fields.values():
                field.required = False
        return fields

    def create(self, validated_data):
        validated_data.pop('id', None)
        client_data = validated_data.pop('get_client', {})
        business = Business.objects.create(**validated_data)
        client_data['content_object'] = business

        self.client = ClientSerializer()
        self.client.create(validated_data=client_data)

        return business

    class Meta:
        model = Business
        fields = "__all__"


class EmployeeSerializer(GenericSerializer):
    user = UserEmployeeSerializer()
    class Meta:
        model = Employee
        fields = "__all__"

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            for field in fields.values():
                field.required = False
        return fields

    def create(self, validated_data):
        validated_data.pop('id', None)
        user_data = validated_data.pop('user', {})
        user_data["username"] = user_data["email"]
        user_data["password"] = "super random password"
        self.user = UserEmployeeSerializer()

        user = self.user.create(validated_data=user_data)
        validated_data['user'] = user

        return Employee.objects.create(**validated_data)


class ProviderRepresentantSerializer(GenericSerializer):
    class Meta:
        model = ProviderRepresentant
        fields = "__all__"


class ProviderSerializer(GenericSerializer):
    representant = ProviderRepresentantSerializer()

    class Meta:
        model = Provider
        fields = "__all__"

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            for field in fields.values():
                field.required = False
        return fields

    def create(self, validated_data):
        validated_data.pop('id', None)
        self.representant = ProviderRepresentantSerializer()
        representant_data = validated_data.pop('representant', {})
        validated_data.pop('business', [])

        representant = self.representant.create(validated_data=representant_data)

        validated_data['representant'] = representant

        provider = Provider.objects.create(**validated_data)

        return provider
