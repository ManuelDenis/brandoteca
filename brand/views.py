import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from brand.forms import NewsletterForm, BrandForm
from brand.models import Newsletter, Brand


class BrandCreate(LoginRequiredMixin, CreateView):
    template_name = 'brand/brand_create.html'
    login_url = '/accounts/login'
    model = Brand
    form_class = BrandForm()
    success_url = '/contact/message_create'

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
            brand = form.save(commit=False)
            brand.user = self.request.user
            brand.save()
            return render(request, 'brand/index.html')
        return render(request, 'brand/brand_create.html', {'form': form})


class BrandUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'brand/brand_create.html'
    login_url = '/accounts/login/'
    model = Brand
    success_url = '/'
    fields = ['name', 'founding_year', 'motto', 'categories', 'entity', 'vat_number', 'reg_no', 'euid', 'address', 'website', 'video_url', 'facebook', 'instagram', 'youtube', 'linkedin', 'logo', 'cover', 'description', 'email', 'phone', 'type', 'main_category', 'country', 'city',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        brand = Brand.objects.filter(user=self.request.user)
        return brand
