from django import forms
from djrichtextfield.widgets import RichTextWidget
import DataChoices.country
from brand.models import Newsletter, Brand
from bt import settings


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']


class BrandForm(forms.ModelForm):
    name = forms.CharField(
        label='Nume brand',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Brand', 'class': 'form-control'}),
        help_text='<ht>Denumirea brandului(Maxim 64 caractere)</ht>'
    )

    description = forms.CharField(
        widget=RichTextWidget(),
        help_text='<ht>Text ce va fi afișat în pagina brandului. Trebuie să aibă între 300 și 2000 de caractere.</ht>'
    )

    email = forms.EmailField(
        label='Adresa de email',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'email@email.ro'}),

    )
    phone = forms.CharField(
        label='Numar de telefon',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '07...'})
    )
    address = forms.CharField(
        label='Adresa sediului',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'adresa'})
    )
    type = forms.ChoiceField(
        label='Tip brand',
        choices=settings.BRAND_TYPES,
        widget=forms.Select(attrs={
            'class': 'bootstrap-select',
            }),
        help_text='<ht>Tipul brandului</ht>'
    )
    motto = forms.ChoiceField(
        label='Slogan',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Slogan'}),
        help_text='<ht>Sloganul brandului. Maxim 200 caractere</ht>'
    )
    founding_year = forms.ChoiceField(
        label='An aparitie brand',
        choices=settings.FOUNDING_YEAR,
        help_text='<ht>Anul infiintarii brandului</ht>'
    )
    main_category = forms.ChoiceField(
        label='Categorie principala',
        choices=DataChoices.country.BRAND_CATEGORY,
        widget=forms.Select(attrs={'placeholder': 'Tip brand*'}),
        help_text='<ht>Categoria principala a brandului</ht>'
    )
    city = forms.ChoiceField(
        label='Orasul sediului',
        required=True,
        choices=DataChoices.country.ORASE
    )
    country = forms.ChoiceField(
        label='Tara',
        required=True,
        choices=DataChoices.country.COUNTRY
    )
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=DataChoices.country.BRAND_CATEGORY,
        label='Categorii suplimentare',
        help_text='<ht>Adauga categorii suplimentare</ht>'
    )
    entity = forms.CharField(
        label='Denumirea identitatii juridice',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'denumire'})
    )
    reg_no = forms.CharField(
        label='Cod unic de inregistrare(CUI)',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'CUI'})
    )
    vat_number = forms.CharField(
        label='Numarul de ordine in registrul comertului',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'numar'})
    )
    euid = forms.CharField(
        label='Identificator unic la nivel european(EUID)',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'EUID'})
    )
    website = forms.URLField(
        label='Website',
        widget=forms.URLInput(attrs={'placeholder': 'website-ul brandului'})
    )
    video_url = forms.URLField(
        label='Video de prezentare',
        widget=forms.URLInput(attrs={'placeholder': 'link de pe youtube'})
    )
    facebook = forms.URLField(
        label='URL Facebook',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de facebook'})
    )
    youtube = forms.URLField(
        label='URL YouTube',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de youtube'})
    )
    linkedin = forms.URLField(
        label='URL Linkedin',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de linkedin'})
    )
    instagram = forms.URLField(
        label='URL Instagram',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de instagram'})
    )

    class Meta:
        model = Brand
        exclude = ['user', 'id', 'is_verified', 'slug', 'created_at', 'updated_at', 'is_active', 'is_verified', 'is_premium', 'is_brand_of_the_month']

