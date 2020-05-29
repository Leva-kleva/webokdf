from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
from django.http import Http404


class AllGalleryView(View):

    def get(self, request):
        '''view all gallery'''
        queryset = Gallery.objects.filter(draft=False)
        return render(request, "gallery/all_gallery_view.html", {"gallery_list": queryset})


class GalleryView(View):

    def get(self, request, pk):
        '''view one gallery'''
        try:
            queryset = Gallery.objects.get(id=pk, draft=False)
        except Gallery.DoesNotExist:
            raise Http404("404")
        return render(request, "gallery/gallery_view.html", {"gallery": queryset})


class ImgView(View):

    def get(self, request, pk):
        '''view one image'''
        try:
            queryset = Image.objects.get(id=pk)
        except Image.DoesNotExist:
            raise Http404("404")
        return render(request, "gallery/image_view.html", {"image": queryset})
