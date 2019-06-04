from django.urls import path

from main.views import (
    main, contacts, about
)

app_name = 'main'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('', main, name='index'),
]
