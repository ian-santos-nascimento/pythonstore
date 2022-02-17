from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('produto/', produtos, name='produto'),
    path('contato/', contato_novo, name='contato'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error404
handler500 = error500