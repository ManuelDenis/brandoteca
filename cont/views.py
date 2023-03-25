from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from brand.models import Brand


class Cont(LoginRequiredMixin, ListView):
    template_name = 'cont/contul_meu.html'
    login_url = '/accounts/login/'
    model = Brand

    def get_queryset(self):
        brand = Brand.objects.filter(user=self.request.user)
        return brand


class BrandurileMele(ListView):
    model = Brand
    template_name = 'cont/brandurile_mele.html'

