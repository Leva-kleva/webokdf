from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
from django.http import Http404

class PeopleView(View):

    def get(self, request):
        '''view all people'''
        try:
            queryset = People.objects.filter(draft=False)
        except People.DoesNotExist:
            raise Http404("404")
        return render(request, "people/people_view.html", {"people_list": queryset})


class ManView(View):

    def get(self, request, pk):
        '''view one people'''
        try:
            queryset = People.objects.get(id=pk, draft=False)
        except People.DoesNotExist:
            raise Http404("404")
        return render(request, "people/man_view.html", {"man": queryset})
