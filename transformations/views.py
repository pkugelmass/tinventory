from django.shortcuts import render
from django.http import HttpResponse
from .models import Transformation, Ministry
from .forms import TransformationFilterForm, TransformationForm
from django.views import generic
from django import forms
from django.core.urlresolvers import reverse_lazy

# LIST VIEW

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
     
# TRANSFORMATION DETAIL VIEWS AND FORMS

class TransformationFormMixin:
     model = Transformation
     form_class = TransformationForm

class TransformationDetail(generic.DetailView):
     model = Transformation

class AddTransformation(TransformationFormMixin, generic.edit.CreateView):
     pass
     
class EditTransformation(TransformationFormMixin, generic.edit.UpdateView):
     pass
     
class DeleteTransformation(generic.edit.DeleteView):
     model = Transformation
     success_url = reverse_lazy('index')