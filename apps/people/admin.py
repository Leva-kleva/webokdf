from django.contrib import admin
from .models import *
from django import forms

#from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "name")
    list_display_links = ("name",)
