from __future__ import absolute_import, unicode_literals
from django.shortcuts import render

from django.db import models

from wagtail.wagtailcore.models import Page



def index(request):
    context = {'slug': 'home'}
    return render(request, 'myblog/index.html', context)