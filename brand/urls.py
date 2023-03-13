from django.urls import path
from brand.views import IndexView, BrandCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('brand_create/', BrandCreate.as_view(), name='brand_create'),
]