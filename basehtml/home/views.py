# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render_to_response,render
from django.core.urlresolvers import reverse
from basehtml.home.models import *

def base(request):
	return render(request, 'base.html', {})

def iletisim(request):
	return render(request, 'contact.html', {})

def index(request):
    return render(request, 'index.html', {})

def hakkimizda(request):
	return render(request, 'hakkimizda.html', {})

def siparis(request):
	return render(request, 'siparis.html', {})

def calisiyoruz(request):
	return render(request, 'calisiyoruz.html', {})

def sorular(request):
	return render(request, 'sorular.html', {})
