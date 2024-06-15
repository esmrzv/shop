from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "catalog/home.html", context)


def contacts(request):
    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product": product
    }
    return render(request, "catalog/product_list.html", context)
