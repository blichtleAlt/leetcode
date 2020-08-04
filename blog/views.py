from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')

def createPageView(request):
    return HttpResponse('create blog post')

def userPageView(request):
    return HttpResponse('User page')

