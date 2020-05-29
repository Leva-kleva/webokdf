from django.db import models
from django.urls import reverse


class People(models.Model):
    name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото", upload_to="people/", blank=True)
    description = models.TextField("Описание", blank=True)
    draft = models.BooleanField("Черновик", default=False)
    order = models.IntegerField("Номер отображения")
    vk = models.CharField("VK", max_length=100, default="-", blank=True)
    inst = models.CharField("Inst", max_length=100, default="-", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''/people/man/'''
        return reverse("man", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Люди"
