from django.shortcuts import render
from django.http import HttpResponse
from .models import Transformation 
from django.views import generic

class IndexView(generic.ListView):
     model = Transformation
     template_name = 'transformations/index.html'

class TransformationDetail(generic.DetailView):
     model = Transformation