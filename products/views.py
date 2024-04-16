from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """A view to show the products page, including sorting and search queries"""  # noqa

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show the individual product details"""  # noqa

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
