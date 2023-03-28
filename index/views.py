from django.shortcuts import render
from django.views.generic import CreateView, ListView
from brand.forms import NewsletterForm
from brand.models import Newsletter, Brand


class IndexView(CreateView, ListView):
    template_name = 'brand/index.html'
    form_class = NewsletterForm
    model = Newsletter
    success_url = '/'

    def get(self, request, *args, **kwargs):
        brands = Brand.objects.all().order_by('-created_at')[:3]
        context = {'form': NewsletterForm(), 'brands': brands}
        return render(request, 'brand/index.html', context)

