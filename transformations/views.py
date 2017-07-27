from django.shortcuts import render
from django.http import HttpResponse
from .models import Transformation 

def index(request):
     context = {'tlist':Transformation.objects.all()}
     return render(request,'transformations/index.html',context)
