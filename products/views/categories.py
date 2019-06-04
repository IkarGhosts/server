import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import (
    ListView, DetailView
)
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from products.forms import ProductForm
from products.models import Category


class CategoryList(ListView):
    model = Category
    template_name = 'categories/list.html'
    paginate_by = 10


class CategoryDetail(DetailView):
    model = Category
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')
        page = self.request.GET.get('page')
        paginator = Paginator(obj.product_set.all(), 10)

        page_obj = paginator.get_page(page)

        return {
            'object': obj,
            'object_list': page_obj.object_list,
            'paginator': paginator,
            'page_obj': page_obj,         
        }


def category_list(request):
    query = get_list_or_404(Category)
    page = request.GET.get('page')
    paginator = Paginator(query, 10)

    categories = paginator.get_page(page)

    return render(request, 'categories/list.html', {'categories': categories})


def category_detail(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    page = request.GET.get('page')
    paginator = Paginator(obj.product_set.all(), 10)

    results = paginator.get_page(page)

    return render(
        request, 
        'categories/detail.html', 
        {
            'object':obj,
            'results': results
        }
    )
