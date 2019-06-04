from django.urls import path

from .views import account_login


app_name = 'accounts'


urlpatterns = [
    path('', account_login, name='login'),
]
