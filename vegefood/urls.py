from django.urls import path, include
from .views import VegefoodView

urlpatterns = [
    path('', VegefoodView.as_view()),
]