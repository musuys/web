from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from product.models import Fruits



def createFruitGet(request):
    return render(request, "product/create.html")


def createFruitPost(request):
    fruit = Fruits()
    fruit.name = request.POST.get('fname', None)
    fruit.descript = request.POST.get('fdescript', None)
    fruit.price = request.POST.get('fprice', None)
    fruit.quantity = request.POST.get('fquantity', None)
    fruit.save()
    for query in connection.queries:
        print(query)
    return HttpResponse('성공')


def readFruitGet(request):
    fruits = Fruits.objects.filter(name='banana', id=3)
    # fruits = Fruits.objects.raw('SELECT * FROM product_fruits')

    context = {
        'fruits': fruits
    }
    return render(request,
                  "product/read.html",
                  context)
