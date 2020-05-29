from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Page
from django.shortcuts import render
from django.http import Http404


'''class PageView(View):

    def get(self, request, slug="/"):
        return render(request, "pages/base.html", {})
        if slug == "/" or slug == "":
            slug = "index"
        try:
            page = Page.objects.get(url=slug, draft=False)
        except Page.DoesNotExist:
            raise Http404("404")
        if slug == "index":
            slug = "base"
#        return render(request, "pages/"+slug+".html", {"page": page})
'''


class PageView(View):

    def get(self, request, slug="/"):
        if slug == "/" or slug == "":
            #slug = "base"
            slug = "default"
            #page = {}
            #return render(request, "pages/"+slug+".html", {"page": page})
        try:
            page = Page.objects.get(url=slug, draft=False)
        except Page.DoesNotExist:
            raise Http404("404")
       # if slug == "index":
        #    slug = "base"
        return render(request, "pages/"+slug+".html", {"page": page})
