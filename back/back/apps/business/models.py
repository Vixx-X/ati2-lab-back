"""
"""
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from phonenumber_field.modelfields import PhoneNumberField
from back.apps.client.models import Client, CommonClient


class CommonBusiness(models.Model):

    name = models.CharField(
        _("name"),
        max_length=255,
    )

    email = models.EmailField(
        _("email"),
    )

    tax_id = models.CharField(
        _("tax id"),
        max_length=255,
    )

    website = models.URLField(
        _("website"),
        max_length=255,
    )

    class Meta:
        app_label = "business"
        db_table = "common_business_data"
        verbose_name = _("business")
        verbose_name_plural = _("businesses")

    def __str__(self):
        return f"Business #{self.id}"


class Business(CommonBusiness):

    services = models.CharField(
        _("services"),
        max_length=255,
    )

    client = GenericRelation(Client)

    @property
    def get_client(self):
        return self.client.first()

    class Meta:
        app_label = "business"
        db_table = "businesses"
        verbose_name = _("business")
        verbose_name_plural = _("businesses")

    def __str__(self):
        return f"Business #{self.id}"


class Employee(CommonClient):

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="employee",
        verbose_name=_("User"),
    )

    document_id = models.CharField(
        _("document id (cedula/rif)"),
        max_length=15,
        validators=[
            validators.RegexValidator(
                regex=r"^[eEvVjJ]\d+$",
                message=_("your document id is not well formatted"),
            ),
        ],
    )

    contract_modality = models.CharField(
        _("contract modality"),
        max_length=255,
    )

    business_email = models.EmailField(
        _("business_email"),
    )

    business = models.ForeignKey(
        "business.CommonBusiness",
        on_delete=models.CASCADE,
        verbose_name=_("Business"),
        related_name="employees",
    )

    local_phone_number = PhoneNumberField(
        _("local phone number"),
        blank=True,
    )

    fav_course = None
    notification_frecuency = None

    class Meta:
        app_label = "business"
        db_table = "employees"
        verbose_name = _("employee")
        verbose_name_plural = _("employees")

    def __str__(self):
        return f"Employee #{self.id}"


class ProviderRepresentant(CommonClient):

    first_name = models.CharField(
        _("first name"),
        max_length=255,
    )

    local_phone = PhoneNumberField(
        _("local phone number"),
        blank=True,
    )

    personal_email = models.EmailField(
        _("notification frecuency"),
    )

    business_email = models.EmailField(
        _("business_email"),
    )

    charge = models.CharField(
        _("charge"),
        max_length=255,
    )

    fav_course = None
    notification_frecuency = None

    class Meta:
        app_label = "business"
        db_table = "provider_representant"
        verbose_name = _("provider_representant")
        verbose_name_plural = _("provider_representants")

    def __str__(self):
        return f"Provider representant #{self.id}"


class Provider(CommonClient):
    name = models.CharField(
        _("name"),
        max_length=255,
    )

    email = models.EmailField(
        _("email"),
    )

    tax_id = models.CharField(
        _("tax id"),
        max_length=255,
    )

    website = models.URLField(
        _("website"),
        max_length=255,
    )

    representant = models.OneToOneField(
        "business.ProviderRepresentant",
        on_delete=models.CASCADE,
    )

    business = models.ManyToManyField(
        "business.Business",
        related_name="providers",
        verbose_name=_("Business"),
    )

    class Meta:
        app_label = "business"
        db_table = "providers"
        verbose_name = _("provider")
        verbose_name_plural = _("providers")

    def __str__(self):
        return f"Provider #{self.id}"
