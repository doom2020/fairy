from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello world')

    def post(self, request, *args, **kwargs):
        pass
