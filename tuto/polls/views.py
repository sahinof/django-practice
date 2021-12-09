from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. This is polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)