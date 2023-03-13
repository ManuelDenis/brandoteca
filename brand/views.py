from django.shortcuts import render
from django.views.generic import CreateView, ListView
from brand.forms import NewsletterForm, BrandForm
from brand.models import Newsletter, Brand


class IndexView(CreateView, ListView):
    template_name = 'brand/index.html'
    form_class = NewsletterForm
    model = Newsletter
    success_url = '/'

    def get(self, request, *args, **kwargs):
        context = {'form': NewsletterForm()}
        return render(request, 'brand/index.html', context)


class BrandCreate(CreateView):
    template_name = 'brand/brand_create.html'
    model = Brand
    form_class = BrandForm
    success_url = '/'
