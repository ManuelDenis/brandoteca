from django.urls import path
from brand.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]