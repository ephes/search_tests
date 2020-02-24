from django.db import models
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _


class Document(models.Model):
    title = models.CharField(_("Title of Document"), blank=True, max_length=255)
    body = models.CharField(_("Body of Document"), blank=True, max_length=2048)
