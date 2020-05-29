from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

import os
from django.utils import timezone


def get_path_upload_image(file, gallery):
    '''создаем папку для сохранения загруженных фото, меняем название'''
    #end_extention = file.split('.')[-1]
    #head = file.split('.')[0]
    #if len(head) > 5:
     #   head = head[:5]
    #file_name = head + '_' + timezone.now().strftime("%h-%m") + '.' + end_extention
    return os.path.join('photos', '{}', '{}').format(gallery, file)


class Image(models.Model):
    '''image'''
    img = models.ImageField("Фото", upload_to="imgs/")
    gallery_name = models.CharField("Название галереи", max_length=100)
    description = RichTextUploadingField("Описание", blank=True)

    def __str__(self):
        return self.img.name

    def get_absolute_url(self):
        '''/gallery/img/<int:pk>/'''
        return reverse("image", kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        self.img.name = get_path_upload_image(self.img.name, self.gallery_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Gallery(models.Model):
    ''' галереи '''
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("главная картинка", upload_to="imgs/main/", blank=True)
    small_description = models.CharField("Краткое описание", max_length=66, blank=True)
    description = RichTextUploadingField("Описание", blank=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    imgs = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''/gallery/<int:pk>/'''
        return reverse("gallery", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
