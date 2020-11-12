from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage
# from .models import Product

from .settings.info import INFO


# Create your views here.
class IndexView(View):
    def get(self, request):
        # contex = INFO.copy()
        context = {}
        context.update(INFO)
        return render(request, 'vegefood/index.html', context)


class ShopView(View):
    def get(self, request, page=1):

        products_list = [
            {
                'name': 'Bell Pepper',
                'image': 'vegefood/images/product-1.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Strawberry',
                'image': 'vegefood/images/product-2.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Green Beans',
                'image': 'vegefood/images/product-3.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Purple Cabbage',
                'image': 'vegefood/images/product-4.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Tomatoe',
                'image': 'vegefood/images/product-5.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Brocolli',
                'image': 'vegefood/images/product-6.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Carrots',
                'image': 'vegefood/images/product-7.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Fruit Juice',
                'image': 'vegefood/images/product-8.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Onion',
                'image': 'vegefood/images/product-9.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Apple',
                'image': 'vegefood/images/product-10.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Garlic',
                'image': 'vegefood/images/product-11.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Chilli',
                'image': 'vegefood/images/product-12.jpg',
                'price': '$120.00'
            }
        ]

        product_on_page = 4
        paginator = Paginator(products_list, product_on_page)

        try:
            products_list = paginator.page(page)
            products_list.page_tuple = tuple(paginator.page_range)
        except EmptyPage:
            # products_list = paginator.get_page(1)
            return redirect(reverse('shop'))

        context = {'page_obj': products_list}
        # context = {'page_obj': Product.objects.all()}
        context.update(INFO)
        return render(request, 'vegefood/shop.html', context)