from django.views.generic import ListView, TemplateView
from brand.models import Brand


class Cont(TemplateView):
    template_name = 'cont/contul_meu.html'


class BrandurileMele(ListView):
    model = Brand
    template_name = 'cont/brandurile_mele'
