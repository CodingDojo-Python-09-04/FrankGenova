# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Hello, I am your first request'
    return HttpResponse(response)

def test(request):
    response = 'This is a test'
    return HttpResponse(response)

def ground_up(request):
    response = "Built from the ground up"
    return HttpResponse(response)

