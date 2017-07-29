from django.shortcuts import render
from django.http import HttpResponse
from .models import Transformation, Ministry
from django.views import generic
from django import forms
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
     model = Transformation
     template_name = 'transformations/index.html'

class TransformationDetail(generic.DetailView):
     model = Transformation

class AddTransformation(generic.edit.CreateView):
     model = Transformation
     fields = ['title','ministry','category','status','description','problem','specific_orgs','primary_contact','tags']
     
class EditTransformation(generic.edit.UpdateView):
     model = Transformation
     fields = ['title','ministry','category','status','description','problem','specific_orgs','primary_contact','tags']
     
class DeleteTransformation(generic.edit.DeleteView):
     model = Transformation
     success_url = reverse_lazy('index')
     