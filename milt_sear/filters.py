from django import forms
from milt_sear.models import *
import django_filters

from django.forms import CheckboxSelectMultiple
# 小部件資料: https://www.kancloud.cn/cyyspring/django/622123

class EmpModelFilter(django_filters.FilterSet):
  empname = django_filters.CharFilter(
    lookup_expr='icontains',
    widget=forms.TextInput(
      attrs={'class': 'form-control text-white', 'placeholder': '姓名'}
    ))

  gender = django_filters.CharFilter(
    widget=forms.Select(
      choices=(('', '請選擇'),) + EmpModel.GENDER_TYPE,
      attrs={'class': 'form-control',
             'placeholder': '',
             }
    )
  )

  occupation = django_filters.ModelMultipleChoiceFilter(
    queryset=Occupation.objects.all(),
    field_name="occupation__name",  # This lets us keep the url as "/?foo=<value>
    # widget=CheckboxSelectMultiple(
    #   attrs={'class': 'form-select form-select-sm pl-0',
    #          }
    # ), 關鍵字
    widget=forms.CheckboxSelectMultiple(
      attrs={'class': 'form-select form-select-sm pl-0',}
    ),
    label="Occupation",
    label_suffix="",
  )
  # ModelChoiceFilter & ForeignKey: https://github.com/carltongibson/django-filter/issues/1023

  salary = django_filters.NumericRangeFilter(field_name="salary", lookup_expr='range', exclude=False)
  # https://www.cnblogs.com/MarsMercury/p/11887566.html


  # 沒作用但是好似可以學習
  @property
  def qs(self):
    parent = super(EmpModelFilter, self).qs
    return parent.order_by("-empname")

  class Meta:
    model = EmpModel
    fields = '__all__'
    # exclude = ('empno')  # 排除
