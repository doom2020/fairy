from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class Home(View):
    def get(self, *args, **kwargs):
        return HttpResponse('hello world home page')

    def post(self, *args, **kwargs):
        pass




