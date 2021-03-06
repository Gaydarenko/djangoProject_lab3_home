from django.urls import path, include
from .views import IndexView, ShopView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page>', ShopView.as_view())
]