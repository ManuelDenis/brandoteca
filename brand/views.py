import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from brand.forms import BrandForm
from brand.models import Brand


class BrandCreate(LoginRequiredMixin, CreateView):
    template_name = 'brand/brand_create.html'
    login_url = '/accounts/login/'
    model = Brand
    form_class = BrandForm()
    success_url = '/contul-meu/'

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
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = self.request.user
            brand.save()
            return render(request, 'brand/index.html')
        return render(request, 'brand/brand_create.html', {'form': form})


@login_required(login_url='accounts/login/')
def brand_upd(request, pk):
    data = Brand.objects.get(id=pk)
    form = BrandForm(instance=data)

    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('contul_meu')
    context = {'form': form}

    return render(request, "brand/brand_create.html", context)
