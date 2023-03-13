from django import forms
from brand.models import Newsletter, Brand


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
