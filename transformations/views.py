from django.http import HttpResponse
from .models import Transformation 

def index(request):
     return HttpResponse(Transformation.objects.all())
