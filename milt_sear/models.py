from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Occupation(models.Model):
  no = models.AutoField(primary_key=True, verbose_name="編號")
  name = models.CharField(max_length=100)

  class Meta:
    ordering = ['-name']
    verbose_name_plural = _('職業名稱')

  def __str__(self):
    return self.name


class EmpModel(models.Model):
  GENDER_TYPE = (
    ("Male", "男"),
    ("Female", "女"),
    ("bisexual", "雙性"),
  )
  empno = models.AutoField(primary_key=True, verbose_name="編號")
  empname = models.CharField(max_length=100, verbose_name="姓名")
  gender = models.CharField(max_length=10, choices=GENDER_TYPE, verbose_name="性別")
  occupation = models.ForeignKey(
    Occupation,
    on_delete=models.CASCADE,
    related_name="empmodels",  # 在外鍵加入 related_name 參數
    null=True, blank=True, default='',
    help_text=_('職務部門'),
    verbose_name="職務",
  )
  salary = models.IntegerField(verbose_name="薪資")

  class Meta:
    db_table = "emp"
    ordering = ['-empno']
    verbose_name_plural = _('搜尋')

  def __str__(self):
    return self.empname
