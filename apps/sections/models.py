from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Sections(models.Model):
    '''Разделы'''
    name = models.CharField("Раздел", max_length=100)
    description = RichTextUploadingField("Описание", blank=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    order = models.IntegerField("Номер отображения")
    link = models.URLField("Ссылка на перенаправление", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''/section/'''
        return reverse("section", kwargs={"slug_sect": self.url})

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class Subsections(models.Model):
    '''подразделы'''
    name = models.CharField("Подраздел", max_length=100)
    description = RichTextUploadingField("Описание", blank=True)
    section = models.ForeignKey(
        Sections, verbose_name="Раздел",  on_delete=models.SET_NULL, null=True
        )
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    order = models.IntegerField("Номер отображения")
    link = models.URLField("Ссылка на перенаправление", blank=True)

    def __str__(self):
        return self.section.name + ", " + self.name

    def get_absolute_url(self):
        '''/section/subsection/'''
        return reverse("subsection", kwargs={"slug_sect": self.section.url, "slug_ssect": self.url})

    class Meta:
        verbose_name = "Подраздел"
        verbose_name_plural = "Подразделы"


class Subsubsections(models.Model):
    '''подподразделы'''
    name = models.CharField("Подподраздел", max_length=100)
    description = RichTextUploadingField("Описание", blank=True)
    section = models.ForeignKey(
        Subsections, verbose_name="Подраздел", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    order = models.IntegerField("Номер отображения")
    link = models.URLField("Ссылка на перенаправление", blank=True)

    def __str__(self):
        return self.section.name + ", " + self.name

    def get_absolute_url(self):
        '''/section/subsection/subsubsection/'''
        return reverse(
                "subsubsection",
                kwargs={"slug_sect": self.section.section.url,
                        "slug_ssect": self.section.url,
                        "slug_sssect": self.url}
                       )

    class Meta:
        verbose_name = "Подподраздел"
        verbose_name_plural = "Подподразделы"
