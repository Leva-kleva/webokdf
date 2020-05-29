from django.contrib import admin
from .models import *


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "img", "gallery_name")
    list_display_links = ("id",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "draft")
    list_display_links = ("name",)
