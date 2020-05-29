# Generated by Django 3.0.6 on 2020-05-29 00:13

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
        ('people', '0001_initial'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='posts/', verbose_name='картинка')),
                ('small_description', models.CharField(blank=True, max_length=66, verbose_name='Краткое описание')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('tip', models.CharField(blank=True, default='Статья', max_length=50, verbose_name='Тип поста')),
                ('datee', models.DateField(blank=True, default=datetime.date(2020, 1, 1), verbose_name='Дата создания')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на перенаправление')),
                ('source', models.URLField(blank=True, verbose_name='Источник')),
                ('source_name', models.CharField(blank=True, max_length=80, verbose_name='Название источника')),
                ('order', models.IntegerField(default=0, verbose_name='порядок')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.People', verbose_name='Автор')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Gallery', verbose_name='Галерея')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sections.Sections', verbose_name='раздел')),
                ('subsection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sections.Subsections', verbose_name='Подраздел')),
                ('subsubsection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sections.Subsubsections', verbose_name='Подподраздел')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
