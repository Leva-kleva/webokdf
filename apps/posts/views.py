from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
from django.http import Http404


class AllPostsView(View):

    def get(self, request):
        try:
            queryset = Post.objects.filter(draft=False).order_by("-order")
        except Post.DoesNotExist:
            raise Http404("404")
        return render(request, "posts/all_posts_view.html", {"posts": queryset})


class PostView(View):

    def get(self, request, slug_post):
        try:
            queryset = Post.objects.get(url=slug_post, draft=False)
            #queryset.gallery = queryset.gallery.order_by("id")
        except Post.DoesNotExist:
            raise Http404("404")
        return render(request, "posts/post_view.html", {"post": queryset})
