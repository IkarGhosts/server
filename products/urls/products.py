from django.urls import path

from products.views import (
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductListView, ProductDetailView,
    product_list, product_detail, product_create,
    product_update, product_delete
)


app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    # path('create/', product_create, name='create'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='list'),
]
