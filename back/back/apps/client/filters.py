from django_filters import rest_framework as filters

from back.apps.client.models import Country, ParticularClient


class ParticularClientFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="client__addresses__country",
        queryset=Country.objects.all(),
    )

    class Meta:
        model = ParticularClient
        fields = ["type"]
