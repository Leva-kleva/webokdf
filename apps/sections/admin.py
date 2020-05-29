from django.contrib import admin
from .models import *
from django import forms

#from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(Sections)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "name", "url")
    list_display_links = ("name",)


@admin.register(Subsections)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "name", "url")
    list_display_links = ("name",)
    list_filter = ("section",)


@admin.register(Subsubsections)
class SubsubsectionAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "name", "section", "url")
    list_display_links = ("name",)
    list_filter = ("section",)
