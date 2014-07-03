from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import *
from app.models import *


def about(request):
  return render(request, 'miscpages/about.html',
      { 'page_active': 0 })

def contact(request):
  return render(request, 'miscpages/contact.html',
      { 'page_active': 0 })