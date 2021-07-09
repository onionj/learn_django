from django.shortcuts import render
from django.views.generic.list import ListView
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


def product_list_views(requests):
    products = Product.objects.all()
    context = {
        'qr': products
    }

    return render(requests, "products/product_list.html", context)
