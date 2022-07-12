from rest_framework import viewsets

from .serializers import BusinessSerializer, EmployeeSerializer, ProviderSerializer
from .models import Business, Employee, Provider


class BusinessViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for businesses
    """

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for employee
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for provider
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
