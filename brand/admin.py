from django.contrib import admin
from brand.models import Newsletter, Brand, Categories


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
