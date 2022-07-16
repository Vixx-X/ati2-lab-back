from rest_framework import viewsets

from back.apps.business.filters import BusinessFilter, EmployeeFilter, ProviderFilter

from .serializers import BusinessSerializer, EmployeeSerializer, ProviderSerializer
from .models import Business, Employee, Provider


class BusinessViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for businesses
    """

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    filterset_class = BusinessFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for employee
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter


class ProviderViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for provider
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filterset_class = ProviderFilter
