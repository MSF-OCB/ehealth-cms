# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, TabbedInterface, ObjectList
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailsearch import index
from wagtailgeowidget.edit_handlers import GeoPanel


class Index(Page):
    intro = RichTextField()
    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro')
    ]
    # Parent page / subpage type rules
    parent_page_types = ['home.HomePage']
    class Meta:
        abstract = True


class GeoContent(Page):
    location = models.PointField(blank=True)
    zoom_map = models.IntegerField(default=5)
    # Editor panels configuration
    content_panels = Page.content_panels + [
        GeoPanel('location'),
    ]
    promote_panels = [
        FieldPanel('zoom_map', classname="full")
    ]
    class Meta:
        abstract = True


class MissionIndex(Index):
    subpage_types = ['ehealth.Mission']

class Mission(GeoContent):
    intro = RichTextField()
    # Editor panels configuration
    content_panels = GeoContent.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['ehealth.MissionIndex']
    subpage_types = ['ehealth.Field']

    @property
    def applications(self):
        applications = []
        for i in self.get_children().all():
            for j in i.specific.applicationFieldUses.all():
                if j.applicationRef not in applications:
                    applications.append(j.applicationRef)
        return applications


class Field(GeoContent):
    intro = RichTextField()

    # Editor panels configuration
    content_panels = GeoContent.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('intro')
    ]

    # Parent page / subpage type rules
    parent_page_types = ['ehealth.Mission']
    subpage_types = []


class ApplicationIndex(Index):
    date = models.DateField("Post date")

    # Editor panels configuration
    content_panels = Index.content_panels + [
        FieldPanel('date'),
    ]
    # Search index configuration
    search_fields = Index.search_fields + [
        index.SearchField('date')
    ]

    # Parent page / subpage type rules
    subpage_types = ['ehealth.Application']


class Application(Page):
    date = models.DateField("Post date")
    pitch = models.TextField(default="")
    intro = RichTextField(default="")
    fields = ParentalManyToManyField('Field',  related_name='applications', blank=True)

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('pitch'),
        FieldPanel('intro', classname="full"),
    ]
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        # ImageChooserPanel('feed_image'),
    ]
    fields_panels = [
        # FieldPanel('fields', widget=forms.CheckboxSelectMultiple),
        InlinePanel('applicationFieldUses', label="Field uses"),

    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(fields_panels, heading='MSF Fields'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])
    # Search index configuration
    search_fields = Page.search_fields + [
        index.FilterField('date'),
        FieldPanel('pitch'),
        index.SearchField('intro'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['ehealth.ApplicationIndex']
    subpage_types = []


class ApplicationFieldUse(models.Model):
    applicationRef = ParentalKey(Application, related_name='applicationFieldUses')
    fieldRef = ParentalKey(Field, related_name='applicationFieldUses')

    panels = [
        FieldPanel('applicationRef'),
        FieldPanel('fieldRef'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['ehealth.Application']
    subpage_types = []

        # class BlogPageRelatedLink(Orderable):
#     page = ParentalKey(BlogPage, related_name='related_links')
#     name = models.CharField(max_length=255)
#     url = models.URLField()
#
#     panels = [
#         FieldPanel('name'),
#         FieldPanel('url'),
#     ]