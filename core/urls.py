from django.urls import path

from .views import *

urlpatterns = [
    path('', Index, name="index"),
    path('produto/<int:pk>', Produtos, name='produto')
]
