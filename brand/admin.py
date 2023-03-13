from django.contrib import admin
from brand.models import Newsletter, Brand


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
