from django.contrib import admin
from .models import *


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "link")
    list_display_links = ("name",)


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "draft")
    list_display_links = ("name",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "name", "url", "draft")
    list_display_links = ("name",)
    list_editable = ("order",)


@admin.register(Sticker)
class StickerAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "color", "draft")
    list_display_links = ("description",)
    list_editable = ("draft",)


@admin.register(Fontans)
class FontansAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "link", "draft")
    list_display_links = ("name",)
    list_editable = ("draft",)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "draft")
    list_display_links = ("description",)
    list_editable = ("draft",)

'''
@admin.register(Zags)
class ZagsAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "name1", "name2")
    list_display_links = ("type",)
'''
