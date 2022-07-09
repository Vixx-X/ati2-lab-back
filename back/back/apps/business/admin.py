from django.contrib import admin
from .models import Business, Employee, Provider

# Register your models here.
admin.site.register(Business)
admin.site.register(Employee)
admin.site.register(Provider)
