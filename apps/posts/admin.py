from django.contrib import admin
from .models import *
from django import forms


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "name", "gallery", "url")
    list_display_links = ("name",)
    list_editable = ("order",)


admin.site.site_title = "Мама, я в телевизоре!"
admin.site.site_header = "Мама, я в телевизоре!"
