# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    
    presencia = Presencia.objects.all()

    return render (request, 'index.html', {'presencia':presencia})
