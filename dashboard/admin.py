from django.contrib import admin
from .models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'email')
  fields = ('name', 'phone', 'email')

  list_filter = ('name',)
  search_fields = ('name',)
  ordering = ('-phone',)


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'category', 'description', 'date_created')
  fields = ('name', 'price', 'category', 'description', 'date_created')

  list_filter = ('name',)
  search_fields = ('name',)
  ordering = ('-price',)


admin.site.register(Product, ProductAdmin)

admin.site.register(Tag)


class OrderAdmin(admin.ModelAdmin):
  list_display = ('customer', 'product', 'date_created', 'status', 'note')
  fields = ('customer', 'product', 'status', 'note')

  list_filter = ('customer',)
  search_fields = ('customer',)
  ordering = ('-product',)


admin.site.register(Order, OrderAdmin)


