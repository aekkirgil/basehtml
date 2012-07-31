# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render_to_response,render
from django.core.urlresolvers import reverse
from basehtml.home.models import *

def base(request):
    nav = 'base'
    
    return render(request, 'base.html', {"nav": nav})

def iletisim(request):
    nav = 'contact'
    
    return render(request, 'contact.html', {"nav": nav})

def index(request):
    nav = 'index'
    
    return render(request, 'index.html', {"nav": nav})

def hakkimizda(request):
    nav = 'about'
    
    return render(request, 'hakkimizda.html', {"nav": nav})

def siparis(request):
    nav = 'order'
    
    return render(request, 'siparis.html', {"nav": nav})

def calisiyoruz(request):
    nav = 'calisiyoruz'
    
    return render(request, 'calisiyoruz.html', {"nav": nav})

def sorular(request):
    nav = 'sorular'
    
    return render(request, 'sorular.html', {"nav": nav})
