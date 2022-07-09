from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
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
    class Meta:
        model = Social
        fields = [
            "name",
            "value",
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

