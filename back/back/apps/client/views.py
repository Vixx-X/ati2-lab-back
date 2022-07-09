from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CountrySerializer, ClientSerializer, ParticularClientSerializer

from .models import Country, Client, ParticularClient

class CountryViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for countries
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ParticularClientViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for particular clients
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ParticularClient.objects.all()
    serializer_class = ParticularClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for clients
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
