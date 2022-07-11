from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

from .models import Client, ParticularClient, Social, Address, Country


class CountrySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="country-detail",
    )
    class Meta:
        model = Country
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    country = serializers.HyperlinkedRelatedField(
        view_name="country-detail",
        queryset=Country.objects.all(),
    )

    class Meta:
        model = Address
        fields = [
            "line1",
            "line2",
            "city",
            "state",
            "country",
            "client",
        ]


class SocialSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Client.objects.all()
    )

    class Meta:
        model = Social
        fields = [
            "name",
            "value",
            "client",
        ]


class ClientSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    socials = SocialSerializer(many=True)
    url = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_url(self, obj):
        return "<WIP>"

    class Meta:
        model = Client
        fields = [
            "url",
            "type",
            "phone_number",
            "fav_course",
            "notification_frecuency",
            "offered_services",
            "addresses",
            "socials",
        ]

    def create(self, validated_data):
        ct = ContentType.objects.get(app_label='client', model='client')
        socials = validated_data.pop("socials")
        addresses = validated_data.pop("addresses")

        validated_data["content_type"] = ct

        client = Client.objects.create(**validated_data)
        
        for social in socials:
            social["client_id"] = client.id
            social["client"] = client.id

        for addres in addresses:
            addres['client'] = client.object_id

        self.socials = SocialSerializer(data=socials, many=True)
        self.addresses = AddressSerializer(data=addresses, many=True)

        if self.addresses.is_valid():
            self.addresses.create(self.addresses.validated_data)

        if self.socials.is_valid():
            self.socials.create(self.socials.validated_data)

        return client


class ParticularClientSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ParticularClient
        fields = [
            "user",
            "type",
            "company",
            "whatsapp",
            "client",
        ]

