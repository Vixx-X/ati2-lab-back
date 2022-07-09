"""
"""
from typing import Literal, Union
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class CommonClient(models.Model):

    phone_number = PhoneNumberField(
        _("phone number"),
        blank=True
    )

    fav_course = models.CharField(
        _("favorite course"),
        max_length=255,
    )

    notification_frecuency = models.CharField(
        _("notification frecuency"),
        max_length=255,
    )

    class Meta:
        app_label = "client"
        db_table = "common_client_data"
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return f"Client #{self.id}"


class Client(CommonClient):

    offered_services = models.CharField(
        _("offered services"),
        max_length=255,
    )

    limit = models.Q(app_label='business', model="Business") | models.Q(app_label="client", model="ParticularClient")

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit,
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    class Meta:
        app_label = "client"
        db_table = "clients"
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return f"Client #{self.id}"

    @property
    def type(self) -> Union[Literal["business"], Literal["particular"]]:
        return "particular" if isinstance(self.content_object, ParticularClient) else "business"


class Social(models.Model):

    name = models.CharField(
        _("social name"),
        max_length=255,
    )

    value = models.CharField(
        _("social value"),
        max_length=255,
    )

    client = models.ForeignKey(
        'client.CommonClient',
        on_delete=models.CASCADE,
        verbose_name=_("Client"),
        related_name="socials",
    )

    class Meta:
        app_label = 'client'
        db_table = "socials"
        verbose_name = _('Social')
        verbose_name_plural = _('Socials')

    def __str__(self):
        return f"{self.name} : {self.value}"


class Country(models.Model):
    """
    `ISO 3166 Country Codes <https://www.iso.org/iso-3166-country-codes.html>`_

    The field names are a bit awkward, but kept for backwards compatibility.
    pycountry's syntax of alpha2, alpha3, name and official_name seems sane.
    """
    iso_3166_1_a2 = models.CharField(
        _('ISO 3166-1 alpha-2'),
        max_length=2,
        primary_key=True,
    )

    iso_3166_1_a3 = models.CharField(
        _('ISO 3166-1 alpha-3'),
        max_length=3,
        blank=True,
    )

    iso_3166_1_numeric = models.CharField(
        _('ISO 3166-1 numeric'),
        blank=True,
        max_length=3,
    )

    #: The commonly used name; e.g. 'United Kingdom'
    printable_name = models.CharField(
        _('Country name'),
        max_length=128,
        db_index=True,
    )

    #: The full official name of a country
    #: e.g. 'United Kingdom of Great Britain and Northern Ireland'
    name = models.CharField(
        _('Official name'),
        max_length=128,
    )

    display_order = models.PositiveSmallIntegerField(
        _("Display order"),
        default=0,
        db_index=True,
        help_text=_('Higher the number, higher the country in the list.'),
    )

    class Meta:
        app_label = 'client'
        db_table = "countries"
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('-display_order', 'printable_name',)

    def __str__(self):
        return self.printable_name or self.name

    @property
    def code(self):
        """
        Shorthand for the ISO 3166 Alpha-2 code
        """
        return self.iso_3166_1_a2

    @property
    def numeric_code(self):
        """
        Shorthand for the ISO 3166 numeric code.

        :py:attr:`.iso_3166_1_numeric` used to wrongly be a integer field, but has to
        be padded with leading zeroes. It's since been converted to a char
        field, but the database might still contain non-padded strings. That's
        why the padding is kept.
        """
        return "%.03d" % int(self.iso_3166_1_numeric)


class Address(models.Model):

    line1 = models.CharField(
        _("First line of address"),
        max_length=255,
    )

    line2 = models.CharField(
        _("Second line of address"),
        max_length=255,
        blank=True,
    )

    city = models.CharField(
        _("City"),
        max_length=255,
        blank=True,
    )

    state = models.CharField(
        _("State/County"),
        max_length=255,
        blank=True,
    )

    country = models.ForeignKey(
        'client.Country',
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
    )

    client = models.ForeignKey(
        'client.CommonClient',
        on_delete=models.CASCADE,
        verbose_name=_("Client"),
        related_name="addresses",
    )

    class Meta:
        app_label = 'client'
        db_table = "addresses"
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return f"address #{self.id}"


class ParticularClient(models.Model):

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name=_("User")
    )

    type = models.CharField(
        _("type"),
        max_length=255,
    )

    company = models.CharField(
        _("company"),
        max_length=255,
    )

    whatsapp = PhoneNumberField(
        _("whatsapp"),
        blank=True
    )

    client = GenericRelation(Client)

    class Meta:
        app_label = "client"
        db_table = "particular_clients"
        verbose_name = _("particular client")
        verbose_name_plural = _("particular clients")

    def __str__(self):
        return f"Particular Client {self.user}"
