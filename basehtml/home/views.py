# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render_to_response,render
from django.core.urlresolvers import reverse

def base(request):
	return render(request, 'base.html', {})

def iletisim(request):
	return render(request, 'contact.html', {})

def index(request):
	return render(request, 'index.html', {})
