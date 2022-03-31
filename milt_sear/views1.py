from django.shortcuts import render
from milt_sear.models import *


# Create your views here.
def milt_sear(request):
  templates_name = "multsearch/index.html"
  # occupations = Occupation.objects.all()
  if request.method == "POST":
    gender = request.POST.get("gender")
    occupation = request.POST.get("occupation")
    empsearchobj = EmpModel.objects.raw(
      'select * from emp where gender = "'+gender+'" and occupation="'+occupation+'"'
    )
    context = {
      "EmpModel": empsearchobj
    }
    return render(request, templates_name, context)
  else:
    empobj = EmpModel.objects.raw('select * from emp')
    context = {
      "title": "Django 123",
      "EmpModel": empobj,
      # "occupations": occupations,
    }
  return render(request, templates_name, context)
