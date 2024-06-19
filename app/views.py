from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sasmita(request):
    return HttpResponse('<h1><marquee>My name is sasmita<marquee><h1>')
