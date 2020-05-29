from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ..gallery.models import Gallery


class People(models.Model):
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("Фото", upload_to="df2020/people", blank=True)
    description = RichTextUploadingField("описание или инструкция")
    link = models.URLField("Ссылка", blank=True)
    draft = models.BooleanField("Черновик", default=False)
    order = models.IntegerField("Номер отображения", default=0)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse("post", kwargs={"slug_post": self.url})

    class Meta:
        verbose_name = "Человек или конкурс"
        verbose_name_plural = "Человеки или конкрусы"


class Sections(models.Model):
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("Обложка", upload_to="df2020/sections/", blank=True)
    description = RichTextUploadingField("описание", blank=True)
    draft = models.BooleanField("Черновик", default=False)
    people = models.ManyToManyField(People, blank=True)
    order = models.IntegerField("Номер отображения", default=0)
    #imgs = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse("post", kwargs={"slug_post": self.url})

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"


class Page(models.Model):
    name = models.CharField("Название", max_length=100)
    image_preview = models.ImageField("Обложка на странице дф2020", upload_to="df2020/", blank=True)
    image = models.ImageField("Обложка на основной странице", upload_to="df2020/page/", blank=True)
    small_description = RichTextUploadingField("Краткое описание", blank=True)
    description = RichTextUploadingField("описание", blank=True)
    draft = models.BooleanField("Черновик", default=False)
    sections = models.ManyToManyField(Sections, blank=True)
    url = models.SlugField(max_length=100, unique=True)
    gallery = models.ForeignKey(
        Gallery, verbose_name="Галерея",  on_delete=models.SET_NULL, null=True, blank=True
        )
    link = models.URLField("Ссылка на перенаправление", blank=True)
    order = models.IntegerField("Номер отображения", default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("page", kwargs={"slug_page": self.url})

    class Meta:
        verbose_name = "Старнциа"
        verbose_name_plural = "Страницы"


class Sticker(models.Model):
    description = models.CharField("содержание", max_length=140)
    color = models.CharField("color", max_length=100, default="red", blank=True)
    draft = models.BooleanField("Черновик", default=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("all_stickers", kwargs={})

    class Meta:
        verbose_name = "Стикер"
        verbose_name_plural = "Стикеры"


class Fontans(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.CharField("Описание", max_length=140)
    color = models.CharField("color", max_length=100, default="red", blank=True)
    link = models.URLField("URL")
    draft = models.BooleanField("Черновик", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = "Встречи"


class History(models.Model):
    description = models.TextField("содержание")
    draft = models.BooleanField("Черновик", default=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"


'''class Zags(models.Model):
    type = models.CharField("тип", max_length=100)
    name1 = models.CharField("Имя 1", max_length=50)
    name2 = models.CharField("Имя 2", max_length=50)

    def __str__(self):
        return self.name1 + " " + self.name2

    class Meta:
        verbose_name = "Загс"
        verbose_name_plural = "Загс"
'''
