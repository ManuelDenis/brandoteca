from django.urls import path
from contact import views

urlpatterns = [
    path('message_create/', views.MessageCreate.as_view(), name='message_create'),
]
