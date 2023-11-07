from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse("Hi how are you")

def jigelrani(request):
    return HttpResponse(('I am Fine'))