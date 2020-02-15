from django.contrib import admin
from .models import Employee, Products, Basket, BasketProducts


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'salary', 'position')
    list_filter = ('position',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'images', 'price', 'date')
    list_filter = ('type',)


class BasketProductsInLine(admin.StackedInline):
    model = BasketProducts
    can_delete = False


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    inlines = [BasketProductsInLine]
