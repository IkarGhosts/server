from django.urls import path

from products.views import (
    CategoryList, CategoryDetail,
    category_list, category_detail
)


app_name = 'categories'

urlpatterns = [
    path('<int:pk>/', CategoryDetail.as_view(), name='detail'),
    path('', CategoryList.as_view(), name='list'),
]
