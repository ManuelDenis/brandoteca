from django.urls import path, include
from brand.views import BrandCreate

urlpatterns = [
    path('creeaza/', BrandCreate.as_view(), name='brand_create'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]
