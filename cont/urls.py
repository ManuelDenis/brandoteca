from django.urls import path
from cont.views import Cont, BrandurileMele

urlpatterns = [
    path('', Cont.as_view(), name='contul_meu'),
    path('brandurile_mele/', BrandurileMele.as_view(), name='brandurile_mele'),
]