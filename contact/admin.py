from django.contrib import admin
from contact.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'message')
