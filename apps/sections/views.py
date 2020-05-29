from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
from django.http import Http404


class AllSectionView(View):

    def get(self, request):
        '''view all sections'''
        try:
            queryset = Sections.objects.filter(draft=False)
        except Sections.DoesNotExist:
            raise Http404("404")
        return render(request, "sections/sections_view.html", {"section_list": queryset})


class SectionView(View):

    def get(self, request, slug_sect):
        '''view subsections'''
        try:
            a = Sections.objects.get(url=slug_sect)
            queryset = Subsections.objects.filter(section=a, draft=False)
        except Subsections.DoesNotExist:
            raise Http404("404")
        # if slug_sect==about: другой шаблон
        return render(request, "sections/sections_view.html", {"section_list": queryset})


class SubsectionView(View):

    def get(self, request, slug_sect, slug_ssect):
        '''view subsubsections'''
        try:
            a = Sections.objects.get(url=slug_sect)
            b = Subsections.objects.get(section=a, url=slug_ssect)
            queryset = Subsubsections.objects.filter(section=b, draft=False)
        except Subsubsections.DoesNotExist:
            raise Http404("404")
        return render(request, "sections/sections_view.html", {"section_list": queryset})


class SubsubsectionView(View):

    def get(self, request, slug_sect, slug_ssect, slug_sssect):
        queryset = {}
        return render(request, "sections/sections_view.html", {"section_list": queryset})
