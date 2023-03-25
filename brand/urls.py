from django.urls import path
from brand.views import BrandCreate, brand_upd

urlpatterns = [
    path('creeaza/', BrandCreate.as_view(), name='brand_create'),
    path('brand_upd/<str:pk>/', brand_upd, name='brand_upd'),
]
