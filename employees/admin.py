from django.contrib import admin
from .models import Employee, Products

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'salary', 'position')
    list_filter = ('position',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'images', 'price', 'date')
    list_filter = ('type',)


