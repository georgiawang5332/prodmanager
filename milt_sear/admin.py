from django.contrib import admin
from milt_sear.models import *


# Register your models here.
class OccupationAdmin(admin.ModelAdmin):
  list_display = ('no', 'name',)
  fields = ('name',)

  list_filter = ('name',)
  search_fields = ('name',)
  ordering = ('-name',)


admin.site.register(Occupation, OccupationAdmin)


class EmpModelAdmin(admin.ModelAdmin):
  list_display = ('empno', 'empname', 'gender', 'occupation', 'salary')
  fields = ('empname', 'gender', 'occupation', 'salary')

  list_filter = ('empname',)
  search_fields = ('empname',)
  ordering = ('-salary',)
  # form = MultSearchForm


admin.site.register(EmpModel, EmpModelAdmin)
