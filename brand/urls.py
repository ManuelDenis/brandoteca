from django.urls import path
from brand.views import BrandCreate

urlpatterns = [
    path('creeaza/', BrandCreate.as_view(), name='brand_create'),
]