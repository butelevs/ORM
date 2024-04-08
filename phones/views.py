from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort_info = request.GET.get("sort", "id")

    if sort_info == "min_price":
        sort_info = "price"
    elif sort_info == "max_price":
        sort_info = "-price"

    context = {
        "phones": Phone.objects.all().order_by(sort_info).values()
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    context = {
        "phone": phone_object
    }
    return render(request, template, context)
