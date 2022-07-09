from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClientConfig(AppConfig):
    name = "back.apps.client"
    label = "client"
    verbose_name = _("client")
