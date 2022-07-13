from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from back.core.serializers import GenericSerializer
from .models import Client, ParticularClient, Social, Address, Country

class CountrySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_img(self, obj):
        code = obj.iso_3166_1_a2
        return f'https://flagcdn.com/w20/{code}.png'

    class Meta:
        model = Country
        fields = "__all__"


class AddressSerializer(GenericSerializer):
    country = serializers.PrimaryKeyRelatedField(
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
        ]


class SocialSerializer(GenericSerializer):
    class Meta:
        model = Social
        fields = [
            "name",
            "value",
        ]


class ClientSerializer(GenericSerializer):
    addresses = AddressSerializer(many=True)
    socials = SocialSerializer(many=True)
    url = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_url(self, obj):
        if obj.type == "business":
            return "<WIP business url>"
        return "<WIP particular client url>"

    class Meta:
        model = Client
        fields = [
            "url",
            "type",
            "phone_number",
            "whatsapp",
            "fav_course",
            "notification_frecuency",
            "offered_services",
            "addresses",
            "socials",
        ]

    def create(self, validated_data):
        validated_data.pop('id', None)
        socials = validated_data.pop("socials")
        addresses = validated_data.pop("addresses")

        client = Client.objects.create(**validated_data)

        for social in socials:
            social["client"] = client

        for address in addresses:
            address['client'] = client

        self.socials = SocialSerializer(many=True)
        self.addresses = AddressSerializer(many=True)

        self.addresses.create(validated_data=addresses)

        self.socials.create(validated_data=socials)

        return client


class ParticularClientSerializer(GenericSerializer):
    client = ClientSerializer(source='get_client')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ParticularClient
        fields = [
            "id",
            "user",
            "type",
            "company",
            "client",
        ]

    def create(self, validated_data):
        validated_data.pop('id', None)
        client_data = validated_data.pop('get_client', {})
        client_data['socials'] = validated_data.pop('socials', [])

        particular_client = ParticularClient.objects.create(**validated_data)

        client_data['content_object'] = particular_client

        self.client = ClientSerializer()
        self.client.create(validated_data=client_data)

        return particular_client
