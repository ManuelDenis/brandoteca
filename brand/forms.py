from allauth.account.forms import SignupForm
from django import forms

import DataChoices.country
from brand.models import Newsletter, Brand
from bt import settings


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']


class BrandForm(forms.ModelForm):
    name = forms.CharField(
        label='Nume brand',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Brand'})
    )
    type = forms.ChoiceField(
        label='Tip brand',
        choices=settings.BRAND_TYPES
        )
    motto = forms.ChoiceField(
        label='Slogan',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Slogan'})
    )
    founding_year = forms.ChoiceField(
        label='An aparitie brand',
        choices=settings.FOUNDING_YEAR
    )
    main_category = forms.ChoiceField(
        label='Categorie principala',
        choices=DataChoices.country.BRAND_CATEGORY
    )
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DataChoices.country.BRAND_CATEGORY,
        label='Categorii'
    )

    class Meta:
        model = Brand
        exclude = ['user', 'id', 'is_verified', 'slug']
