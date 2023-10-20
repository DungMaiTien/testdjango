from django.urls import path
from .views import add_to_cart

from . import views

app_name = "product1"
urlpatterns = [
    path('', views.product1, name = "product1"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
