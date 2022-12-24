from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def third(request):
    return HttpResponse('<h1><i>These release notes describe issues specific to the Git for Windows release. The release notes covering the history of the core git commands can be found in the Git project.</i></h1>')
    
def forth(request):
    return HttpResponse('<h1><i><marquee>Changes in v2.39.0since v2.38.1 (October 18th 2022)</marquee></i><h1>')
    