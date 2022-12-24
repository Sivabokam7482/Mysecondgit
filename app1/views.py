from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('This is a input of the Httpresponse')
    
def second(request):
    return HttpResponse('<b>I am talking in telugu</b>')