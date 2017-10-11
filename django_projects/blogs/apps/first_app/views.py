'''
methods used for http response in blogs project

Created: 10/10/2017
Author: Frank J Genova
'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    '''
    / - display "placeholder to later display all the list of blogs"
    via HttpResponse. Have this be handled by a method named 'index'.
    '''

    response = 'Placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(request):
    '''
    /new - display "placeholder to display a new form to create a new blog"
    via HttpResponse.  Have this be handled by a method named 'new'.
    '''

    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    '''
    /create - Have this be handled by a method named 'create'.
    For now, have this url redirect to /.
    '''

    return redirect('/')

def show(request, number):
    '''
    /{{number}} - display 'placeholder to display blog {{number}}.
    For example /15 should display a message 'placeholder to display blog 15'.
    Have this be handled by a method named 'show'.
    '''

    response = 'placeholder to display blog {}.'.format(number)
    return HttpResponse(response)

def edit(request, number):
    '''
    /{{number}}/edit - display 'placeholder to edit blog {{number}}.
    Have this be handled by a method named 'edit'.
    '''

    response = ('placeholder to edit blog {}'.format(number))
    return HttpResponse(response)

def destroy(request, number):
    '''
    /{{number}}/delete - Have this be handled by a method named 'destroy'.
    For now, have this url redirect to /.
    '''
    return redirect('/')
