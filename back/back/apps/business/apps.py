from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BusinessConfig(AppConfig):
    name = "back.apps.business"
    label = "business"
    verbose_name = _("business")
