import datetime
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from brand.forms import NewsletterForm, BrandForm
from brand.models import Newsletter, Brand


class BrandCreate(CreateView):
    template_name = 'brand/brand_create.html'
    model = Brand
    form_class = BrandForm()
    success_url = '/'

    def get(self, request, *args, **kwargs):
        choice = {
            'type': 'Brand comercial',
            'main_category': 'Administratie / Sector Public',
            'country': 'Romania',
            'founding_year': int(datetime.datetime.now().year),
        }
        context = {'form': BrandForm(initial=choice)}
        return render(request, 'brand/brand_create.html', context)

    def post(self, request, *args, **kwargs):
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            brand.save()
            return render(request, '/')
        return render(request, 'brand/brand_create.html', {'form': form})
