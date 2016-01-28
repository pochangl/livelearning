from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("<html><head></head><body>I am home page</body></html>")