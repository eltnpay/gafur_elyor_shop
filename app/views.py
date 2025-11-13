from django.shortcuts import render
from .models import Product
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
# Create your views here.



def product_list(request):
    products = Product.objects.all()  # достаём все записи из таблицы Product
    return render(request, 'product_list.html', {'products': products})