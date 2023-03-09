from django.shortcuts import render
from django.views.generic import CreateView
from brand.forms import NewsletterForm
from brand.models import Newsletter


class IndexView(CreateView):
    template_name = 'brand/index.html'
    form_class = NewsletterForm
    model = Newsletter

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)

