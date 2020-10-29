from django.shortcuts import render
from django.views import View
from .settings.info import INFO


# Create your views here.
class IndexView(View):
    def get(self, request):
        # contex = INFO.copy()
        contex = {}
        contex.update(INFO)
        return render(request, 'vegefood/index.html', contex)


class ShopView(View):
    def get(self, request):
        contex = INFO.copy()
        return render(request, 'vegefood/shop.html', contex)