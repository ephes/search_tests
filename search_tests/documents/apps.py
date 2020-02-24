from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DocumentsConfig(AppConfig):
    name = "search_tests.documents"
    verbose_name = _("Documents")
