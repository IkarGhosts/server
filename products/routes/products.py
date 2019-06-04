from django.urls import path

from products.views import ProductJsonListView


app_name = 'rest_products'

urlpatterns = [
    path('', ProductJsonListView.as_view(), name='list'),
]
