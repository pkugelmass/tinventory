from django.shortcuts import render
from django.http import HttpResponse
from .models import Transformation, Ministry
from .forms import TransformationFilterForm
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
     
def IndexView(request):
     
     form = TransformationFilterForm()
     query_set = Transformation.objects.all()
     
     if request.GET:
          
          # Format the input into keyword arguments (eg. category:structure)
          criteria = { a.lower():request.GET[a] for a in request.GET if request.GET[a] != ''}
          
          # Filter the query based on those arguments (if any).
          query_set = query_set.filter(**criteria)
          
          # Set the forms to show the criteria used when they are reloaded.
          for fieldname in criteria:
               form.fields[fieldname].initial = criteria[fieldname]

     package = {
          'transformation_list' : query_set,
          't_filter_form' : form,
     }
     
     return render(request, 'transformations/index.html', package)