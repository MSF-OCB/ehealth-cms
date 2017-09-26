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
    subpage_types = ['ehealth.FieldProject']

class FieldProject(GeoContent):
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


class ToolIndex(Index):
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
    subpage_types = ['ehealth.Tool']


class Tool(Page):
    date = models.DateField("Post date")
    pitch = models.TextField(default="")
    intro = RichTextField(default="")
    projects = ParentalManyToManyField('FieldProject',  related_name='tools', blank=True)


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
    projects_panels = [
        FieldPanel('projects', widget=forms.CheckboxSelectMultiple),
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(projects_panels, heading='Projects'),
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
    parent_page_types = ['ehealth.ToolIndex']
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