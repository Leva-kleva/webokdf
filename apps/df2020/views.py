from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
from ..gallery.models import Gallery
from .forms import *
from django.shortcuts import redirect
from django.http import Http404, HttpResponse
from random import randint


class AllContentView(View):

    def get(self, request):
        try:
            queryset = Page.objects.filter(draft=False).order_by("order")
        except Page.DoesNotExist:
            raise Http404("404")
        return render(request, "df2020/base.html", {"content_list": queryset})


class PageView(View):

    def get(self, request, slug_page):
        try:
            queryset = Page.objects.get(draft=False, url=slug_page)
        except Page.DoesNotExist:
            raise Http404("404")
        return render(request, "df2020/page.html", {"page": queryset})

'''
class ParadeView(View):

    def get(self, request):
        queryset = Sticker.objects.filter(draft=False).order_by('-id')[:10]
        return render(request, "df2020/parade.html", {"stickers": queryset})
'''
'''
class RetroView(View):

    def get(self, request):
        queryset = Gallery.objects.get(url="retro", draft=False)
        return render(request, "gallery/unique/retro.html", {"retro": queryset})
        #return render(request, "gallery/gallery_view.html", {"gallery": queryset})

'''
colors = ["red", "yellow", "green", "blue", "purple"]
class AddStickerView(View):

    def post(self, request):
        form = StickerForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.color = colors[randint(0, 4)]
            form.save()
        return redirect('/df2020/wishes')


class AllStickersView(View):

    def get(self, request):
        queryset = Sticker.objects.filter(draft=False).order_by("-id")
        return render(request, "df2020/all_stickers.html", {"stickers": queryset})


class FontansView(View):

    def get(self, request):
        queryset = Fontans.objects.filter(draft=False).order_by("-id")
        return render(request, "df2020/fontans.html", {"fontans": queryset})


class AddFontansView(View):

    def post(self, request):
        form = FontanForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.color = colors[randint(0, 4)]
            form.save()
        return redirect('/df2020/fontan')


class AddHistoryView(View):

    def post(self, request):
        form = HistoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/df2020/stream')


'''class AddZagsView(View):

    def post(self, request):
        form = ZagsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/df2020/contests')
'''