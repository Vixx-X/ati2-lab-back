from django_filters import rest_framework as filters

from back.apps.client.models import Country, ParticularClient


class ParticularClientFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="client__addresses__country",
        queryset=Country.objects.all(),
    )

    type = filters.CharFilter(
        field_name="type",
        lookup_expr="icontains",
    )

    class Meta:
        model = ParticularClient
        fields = []
