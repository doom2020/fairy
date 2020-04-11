from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class Register(View):
    def get(self, *args, **kwargs):
        return HttpResponse('hello world register')

    def post(self, *args, **kwargs):
        pass
