from django_filters import rest_framework as filters

from back.apps.business.models import Business, Employee, Provider
from back.apps.client.models import Country


class BusinessFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="client__addresses__country",
        queryset=Country.objects.all(),
    )

    class Meta:
        model = Business
        fields = ["name"]


class EmployeeFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="addresses__country",
        queryset=Country.objects.all(),
    )

    class Meta:
        model = Employee
        fields = ["contract_modality"]


class ProviderFilter(filters.FilterSet):

    country = filters.ModelChoiceFilter(
        field_name="addresses__country",
        queryset=Country.objects.all(),
    )

    representant_country = filters.ModelChoiceFilter(
        field_name="representant__addresses__country",
        queryset=Country.objects.all(),
    )

    class Meta:
        model = Provider
        fields = ["name"]
