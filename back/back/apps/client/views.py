from rest_framework import viewsets

from back.apps.client.filters import ParticularClientFilter

from .serializers import CountrySerializer, ClientSerializer, ParticularClientSerializer

from .models import Country, Client, ParticularClient


class CountryViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for countries
    """

    http_method_names = ["get", "options", "head"]
    lookup_field = "iso_3166_1_a2"
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ParticularClientViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for particular clients
    """

    queryset = ParticularClient.objects.all()
    serializer_class = ParticularClientSerializer
    filterset_class = ParticularClientFilter


class ClientViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for clients
    """

    http_method_names = ["get", "options", "head"]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
