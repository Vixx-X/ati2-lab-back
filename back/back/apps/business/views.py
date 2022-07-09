from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import BusinessSerializer, EmployeeSerializer, ProviderSerializer
from .models import Business, Employee, Provider


class BusinessViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for businesses
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for employee
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for provider
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
