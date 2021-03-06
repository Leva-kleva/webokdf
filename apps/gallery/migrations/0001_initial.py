# Generated by Django 3.0.6 on 2020-05-29 00:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='imgs/', verbose_name='Фото')),
                ('gallery_name', models.CharField(max_length=100, verbose_name='Название галереи')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='imgs/main/', verbose_name='главная картинка')),
                ('small_description', models.CharField(blank=True, max_length=66, verbose_name='Краткое описание')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('imgs', models.ManyToManyField(to='gallery.Image')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
            },
        ),
    ]
