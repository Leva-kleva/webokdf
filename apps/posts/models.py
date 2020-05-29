from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ..gallery.models import Gallery
from ..sections.models import *
from ..people.models import *
from datetime import date


class Post(models.Model):
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("картинка", upload_to="posts/", blank=True)
    small_description = models.CharField("Краткое описание", max_length=66, blank=True)
    description = RichTextUploadingField("Описание", blank=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    tip = models.CharField("Тип поста", default="Статья", blank=True, max_length=50)
    #data = models.CharField("Дата", max_length=40, blank=True)
    datee = models.DateField("Дата создания", default=date(2020, 1, 1), blank=True)

    gallery = models.ForeignKey(
        Gallery, verbose_name="Галерея",  on_delete=models.SET_NULL, null=True, blank=True
        )
    section = models.ForeignKey(
        Sections, verbose_name="раздел", on_delete=models.SET_NULL, null=True
    )
    subsection = models.ForeignKey(
        Subsections, verbose_name="Подраздел", on_delete=models.SET_NULL, null=True
    )
    subsubsection = models.ForeignKey(
        Subsubsections, verbose_name="Подподраздел", on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        People, verbose_name="Автор", on_delete=models.SET_NULL, null=True, blank=True
    )
    link = models.URLField("Ссылка на перенаправление", blank=True)
    source = models.URLField("Источник", blank=True)
    source_name = models.CharField("Название источника", max_length=80, blank=True)
    order = models.IntegerField("порядок", default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''/posts/<slug:slug_post>/'''
        return reverse("post", kwargs={"slug_post": self.url})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
