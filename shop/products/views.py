from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
# Create your views here.

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(
            *args, **kwargs)

        print(context)
        return context


def product_list_view(requests):
    products = Product.objects.all()
    context = {
        'object_list': products
    }

    return render(requests, "products/product_list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        return context


def product_detail_view(request, productId=None, *args, **kwargs):
    # try:
    #     product = Product.objects.get(id=productId)
    # except Product.DoesNotExist:
    #     raise Http404("product does not found from try except")
    # except:
    #     print("what?")

    qs = Product.objects.filter(id=productId)
    # print(qs)
    if qs.exists() and qs.count() == 1:
        product = qs.first()
    else:
        raise Http404("product does not found _______")

    # product = get_object_or_404(Product, id=productId)
    context = {
        "object": product
    }

    return render(request, "products/product_detail.html", context)
