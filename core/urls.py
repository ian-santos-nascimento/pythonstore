from django.urls import path
from django.conf.urls import handler404, handler500
from .views import *

urlpatterns = [
    path('', Index, name="index"),
    path('produto/<int:pk>', Produtos, name='produto')
]

handler404 = error404
handler500 = error500