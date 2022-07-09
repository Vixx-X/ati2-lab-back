from django.contrib import admin
from .models import Client, Social, Country, Address, ParticularClient

# Register your models here.
admin.site.register(Client)
admin.site.register(Social)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(ParticularClient)
