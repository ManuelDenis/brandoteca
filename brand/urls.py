from django.urls import path, include
from brand.views import BrandCreate, BrandUpdate

urlpatterns = [
    path('creeaza/', BrandCreate.as_view(), name='brand_create'),
    path('brand_update/<str:pk>', BrandUpdate.as_view(), name='brand_update'),
]
