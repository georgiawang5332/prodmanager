from django.shortcuts import render
from milt_sear.models import *
from .filters import *

# Create your views here.
def milt_sear(request):
  templates_name = "multsearch/index.html"
  occupations = Occupation.objects.all()
  empmodel = EmpModel.objects.all()

  empmodelFilter = EmpModelFilter(queryset=empmodel)

  if request.method == "POST":
    empmodelFilter = EmpModelFilter(request.POST, queryset=empmodel)

  context = {
    "title": "Django 123",
    "occupations": occupations,
    'empmodelFilter': empmodelFilter,
  }

  return render(request, templates_name, context)
