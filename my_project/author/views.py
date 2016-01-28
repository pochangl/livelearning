from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("<html><head></head><body>I am home page</body></html>")

def param(request, *args, **kwargs):
    return HttpResponse(str(kwargs))


def reverse_view(request, *args, **kwargs):

    return HttpResponse(reverse('author:user_page', kwargs={"user_id": "99"}))