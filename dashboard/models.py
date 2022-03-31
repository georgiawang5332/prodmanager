from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Customer(models.Model):
  name = models.CharField(max_length=200, null=True, verbose_name="姓名")
  phone = models.CharField(max_length=200, null=True, verbose_name="電話")
  email = models.CharField(max_length=200, null=True, verbose_name="信箱")
  date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="建立日期")

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['-phone']
    verbose_name_plural = _('顧客')


class Tag(models.Model):
  name = models.CharField(max_length=200, null=True, verbose_name="姓名")

  def __str__(self):
    return self.name
  class Meta:
    ordering = ['-name']
    verbose_name_plural = _('標籤')


class Product(models.Model):
  CATEGORY = (
    ('Indoor', 'Indoor'),  # 室內的
    ('Out Door', 'Out Door'),  # 室外的
  )

  name = models.CharField(max_length=200, null=True, verbose_name="姓名")
  price = models.FloatField(null=True, verbose_name="價錢")
  category = models.CharField(max_length=200, null=True, choices=CATEGORY, verbose_name="類別")
  description = models.CharField(max_length=200, null=True, blank=True, verbose_name="描述")
  date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="標籤")
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['-date_created']
    verbose_name_plural = _('商品')


class Order(models.Model):
  STATUS = (
    ('Pending', 'Pending'),  # 待定; 未繳錢
    ('OutForDelivery', 'OutForDelivery'),  # 交貨外; 已繳錢未取貨
    ('Delivered', 'Delivered'),  # 已交付; 已取貨
  )

  customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, verbose_name="顧客")
  product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, verbose_name="商品")
  date_created = models.DateTimeField(_('建立日期'),auto_now_add=True, null=True)
  status = models.CharField(_('狀態'),max_length=200, null=True, choices=STATUS)
  note = models.CharField(_('備註'), max_length=1000, null=True)

  def __str__(self):
    return self.product.name
  class Meta:
    ordering = ['-date_created']
    verbose_name_plural = _('訂購')
