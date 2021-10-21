from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.conf import settings
# Create your views here.


def homepage(request):
    return render(request, 'pages/index.html', {'cart': cart(request),
                                                'count': count(request)})


def store(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    brand = None
    brands = Brand.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.objects.filter(category=category)
    cart_product_form = CartAddProductForm()
    cart_items = request.session.get(settings.CART_SESSION_ID)
    pr = []
    if cart_items:
        product = cart_items.keys()
        pr = Product.objects.filter(id__in=product)
    return render(request, 'pages/store.html', {'category': category,
                                                'categories': categories,
                                                'products': products,
                                                'cart_product_form': cart_product_form,
                                                'cart': cart(request),
                                                'cart_items': pr,
                                                'count': count(request),
                                                })


def product(request,  product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/product.html', {'product': product,
                                                  'cart_product_form': cart_product_form,
                                                  'cart': cart(request),
                                                  'count': count(request),
                                                  })


def count(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    count = 0
    if cart:
        cart_values = cart.values()
        for item in cart_values:
            count += item['quantity']
    return count


def cart(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    count = 0
    subtotal = 0
    product_list = []
    if cart:
        cart_values = cart.values()
        for item in cart_values:
            count += item['quantity']
            subtotal += item['quantity']*float(item['price'])
        cart_items_id = cart.keys()
        product_list = Product.objects.filter(id__in=cart_items_id)

    return {'count': count, 'product_list': product_list, 'cart': cart, 'subtotal': subtotal}
