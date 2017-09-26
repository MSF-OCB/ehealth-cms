from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel, FieldPanel

from wagtail.wagtailcore.models import Page


class HomePage(Page):
    pass