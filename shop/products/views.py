from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
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
        'qr': products
    }

    return render(requests, "products/product_list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        context['abc'] = "this is my test data in context"
        print(context)
        return context


def product_detail_view(request, productId=None, *args, **kwargs):
    # product = Product.objects.get(id=productId)
    product = get_object_or_404(Product, id=productId)
    context = {
        "object": product
    }

    return render(request, "products/product_detail.html", context)
