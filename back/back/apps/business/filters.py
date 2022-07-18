from django_filters import rest_framework as filters

from back.apps.business.models import Business, Employee, Provider
from back.apps.client.models import Country


class BusinessFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="client__addresses__country",
        queryset=Country.objects.all(),
    )

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Business
        fields = []


class EmployeeFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="addresses__country",
        queryset=Country.objects.all(),
    )

    contract_modality = filters.CharFilter(
        field_name="contract_modality",
        lookup_expr="icontains",
    )

    class Meta:
        model = Employee
        fields = []


class ProviderFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="addresses__country",
        queryset=Country.objects.all(),
    )

    representant_country = filters.ModelChoiceFilter(
        field_name="representant__addresses__country",
        queryset=Country.objects.all(),
    )

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Provider
        fields = []
